"""Async subprocess wrappers for Powerpipe and Steampipe CLIs.

All functions invoke the CLI via asyncio.create_subprocess_exec,
parse JSON from stdout, and return structured dicts.

Steampipe lifecycle is NOT managed here — it must already be running.
"""

import asyncio
import json
import os
import re


class PowerpipeError(Exception):
    """Raised when a powerpipe command fails (exit code > 1)."""


class SteampipeError(Exception):
    """Raised when a steampipe query command fails."""


def _powerpipe_env() -> dict[str, str]:
    """Subprocess env with update check disabled."""
    env = os.environ.copy()
    env["POWERPIPE_UPDATE_CHECK"] = "false"
    return env


async def _run_powerpipe(*args: str, mod_location: str, allow_alarm: bool = False) -> str:
    """Run a powerpipe command and return stdout.

    allow_alarm: if True, treat exit code 1 (alarms) and 2 (errors) as success —
    the JSON output contains the error details per-control.
    """
    cmd = ["powerpipe", *args, "--mod-location", mod_location]
    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        env=_powerpipe_env(),
    )
    stdout, stderr = await proc.communicate()
    rc = proc.returncode
    if rc != 0 and not (allow_alarm and rc in (1, 2)):
        msg = stderr.decode().strip() or stdout.decode().strip() or f"exit code {rc}"
        raise PowerpipeError(msg)
    return stdout.decode()


async def list_benchmarks(mod_location: str) -> list[dict]:
    """List all benchmarks in a Powerpipe mod."""
    raw = await _run_powerpipe("benchmark", "list", "--output", "json", mod_location=mod_location)
    return json.loads(raw)


def _unwrap_show(raw_json: str) -> dict:
    """Unwrap powerpipe show output — returns a single-element array, we want the dict."""
    items = json.loads(raw_json)
    return items[0] if isinstance(items, list) and len(items) == 1 else items


async def show_benchmark(qualified_name: str, mod_location: str) -> dict:
    """Show detailed info about a specific benchmark."""
    raw = await _run_powerpipe("benchmark", "show", qualified_name, "--output", "json", mod_location=mod_location)
    return _unwrap_show(raw)


async def list_controls(mod_location: str) -> list[dict]:
    """List all controls in a Powerpipe mod."""
    raw = await _run_powerpipe("control", "list", "--output", "json", mod_location=mod_location)
    return json.loads(raw)


async def show_control(qualified_name: str, mod_location: str) -> dict:
    """Show detailed info about a specific control (description, SQL, tags, severity)."""
    raw = await _run_powerpipe("control", "show", qualified_name, "--output", "json", mod_location=mod_location)
    return _unwrap_show(raw)


async def list_queries(mod_location: str) -> list[dict]:
    """List all named queries in a Powerpipe mod with their SQL."""
    raw = await _run_powerpipe("query", "list", "--output", "json", mod_location=mod_location)
    return json.loads(raw)


async def list_mods(mod_location: str) -> list[dict]:
    """List all mods (root + dependencies) in a Powerpipe workspace."""
    raw = await _run_powerpipe("mod", "list", "--output", "json", mod_location=mod_location)
    return json.loads(raw)


async def show_query(qualified_name: str, mod_location: str) -> dict:
    """Show detailed info about a named query (title, description, SQL)."""
    raw = await _run_powerpipe("query", "show", qualified_name, "--output", "json", mod_location=mod_location)
    return _unwrap_show(raw)


async def list_variables(mod_location: str) -> list[dict]:
    """List all variables in a Powerpipe mod."""
    raw = await _run_powerpipe("variable", "list", "--output", "json", mod_location=mod_location)
    return json.loads(raw)


async def show_variable(qualified_name: str, mod_location: str) -> dict:
    """Show detailed info about a variable (type, default, value, description)."""
    raw = await _run_powerpipe("variable", "show", qualified_name, "--output", "json", mod_location=mod_location)
    return _unwrap_show(raw)


async def run_benchmark(qualified_name: str, mod_location: str, *, dry_run: bool = False, **kwargs: str) -> dict:
    """Run a benchmark. If dry_run=True, enumerate controls without executing.

    Exit code 1 (alarms found) is treated as success — the result contains findings.
    Exit code >1 is an error.

    kwargs are passed as --key value CLI flags (e.g., tag="key=value", var="key=value").
    """
    args = ["benchmark", "run", qualified_name, "--output", "json", "--progress=false"]
    if dry_run:
        args.append("--dry-run")
    for key, value in kwargs.items():
        args.extend([f"--{key}", value])
    raw = await _run_powerpipe(*args, mod_location=mod_location, allow_alarm=True)
    return json.loads(raw)


async def run_control(qualified_name: str, mod_location: str, **kwargs: str) -> dict:
    """Run a single control and return full results.

    Exit code 1 (alarms found) is treated as success.
    """
    args = ["control", "run", qualified_name, "--output", "json", "--progress=false"]
    for key, value in kwargs.items():
        args.extend([f"--{key}", value])
    raw = await _run_powerpipe(*args, mod_location=mod_location, allow_alarm=True)
    return json.loads(raw)


def format_command(*args: str, mod_location: str | None = None) -> str:
    """Format a powerpipe CLI command string for debug output."""
    parts = ["powerpipe", *args]
    if mod_location:
        parts.extend(["--mod-location", mod_location])
    return " ".join(parts)


async def query(sql: str, *, database: str | None = None, limit: int = 25) -> dict:
    """Run an arbitrary SQL query via steampipe query.

    Appends LIMIT if not already present in the SQL. Default 25 rows to keep
    responses compact for LLM consumption. Caller can override with a higher limit.
    Returns {columns: [...], rows: [...]}.
    database: Postgres connection string. Defaults to localhost:9193.
    """
    # Append LIMIT if not already present
    if not re.search(r"\bLIMIT\b", sql, re.IGNORECASE):
        sql = f"{sql.rstrip().rstrip(';')} LIMIT {limit}"

    cmd = ["steampipe", "query", sql, "--output", "json"]
    if database:
        cmd.extend(["--database", database])

    proc = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        msg = stderr.decode().strip() or stdout.decode().strip() or f"exit code {proc.returncode}"
        raise SteampipeError(msg)
    return json.loads(stdout.decode())