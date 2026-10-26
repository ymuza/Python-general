"""Ejercicio práctico: sistema de plugins con registro por decorador y una factoría."""

from abc import ABC, abstractmethod
from typing import Any


_plugins: dict[str, type["BasePlugin"]] = {}


def plugin(cls: type["BasePlugin"]) -> type["BasePlugin"]:
    """Decorador que registra la clase en el contenedor global, usando cls.name como clave."""
    _plugins[cls.name] = cls
    return cls


class BasePlugin(ABC):
    """ Lógica común a todos los plugins.
    - Los plugins deben tener configuración interna.
    - Los plugins pueden ser habilitados o deshabilitados solamente usando
      los métodos enable y disable.
    """

    name: str = "BasePlugin"

    def __init__(self, **config: Any) -> None:
        self.config = config
        self._enabled = True

    @property
    def is_enabled(self) -> bool:
        """Checkea si el plugin esta habilitado."""
        return self._enabled

    def enable(self) -> None:
        """Marca el plugin como habilitado."""
        self._enabled = True

    def disable(self) -> None:
        """Marca el plugin como deshabilitado."""
        self._enabled = False

    @abstractmethod
    def run(self) -> Any:
        """Ejecuta la lógica del plugin y devuelve un valor."""
        raise NotImplementedError


class PluginFactory:
    """Factoría de plugins."""

    @staticmethod
    def create(name: str, strict: bool = False, **config: Any) -> BasePlugin | None:
        """
        Devuelve una instancia del plugin solicitado.

        - strict determina si se debe levantar una excepcion si el tipo de plugin no existe.
        """
        plugin_cls = _plugins.get(name)
        if plugin_cls is None:
            if strict:
                raise KeyError(f"no hay un plugin registrado con el nombre '{name}'")
            return None
        return plugin_cls(**config)


@plugin
class GreetingPlugin(BasePlugin):
    """Saluda a la persona indicada. Config esperado: user='...'. """

    name = "GreetingPlugin"

    def run(self) -> dict:
        """Retorna {'message': 'Hello, <user>!'}."""
        user = self.config.get("user", "world")
        return {"message": f"Hello, {user}!"}


# Ejemplo de uso
if __name__ == "__main__":
    plugin_inst = PluginFactory.create("GreetingPlugin", user="Ada", strict=True)
    print(plugin_inst.run())          # → {'message': 'Hello, Ada!'}
    plugin_inst.disable()
    print("¿Habilitado?", plugin_inst.is_enabled)
    plugin_inst.enable()
    print("¿Habilitado?", plugin_inst.is_enabled)
