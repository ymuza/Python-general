"""Renders a Jinja2 HTML template and converts it to PDF with WeasyPrint."""

from pathlib import Path

# jinja2 and weasyprint are optional deps: install with `poetry install --with reports`
try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    from weasyprint import HTML
except ImportError as exc:
    raise SystemExit(
        f"Missing optional dependency ({exc.name}). Run: poetry install --with reports"
    ) from exc

BASE_DIR = Path(__file__).parent

# Load the Jinja2 template environment (templates live next to this script)
env = Environment(
    loader=FileSystemLoader(BASE_DIR),
    autoescape=select_autoescape(["html"]),
)

# Define the context variables
context = {
    'title': 'My Document',
    'heading': 'Welcome to my website!',
    'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
}

# Render the template with Jinja2
template = env.get_template('template1.html')
html_out = template.render(**context)

# Convert the HTML to PDF with WeasyPrint
HTML(string=html_out).write_pdf(BASE_DIR / 'output.pdf')
