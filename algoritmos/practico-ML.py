
from abc import ABC, abstractmethod
from typing import Any, Dict, Optional



_plugins: Dict[str, "BasePlugin"] = {}

# class PluginError(Exception):
#     """Excepción base para errores de plugin."""
#
#
# class PluginNotFound(PluginError):
#     """Se lanza cuando no existe un plugin registrado con el nombre pedido."""
#
#
# class PluginExecutionError(PluginError):
#     """Se lanza cuando la ejecución de un plugin produce un fallo."""
#
#
def plugin(cls: "BasePlugin"):
    """Decorador que registra la clase en el contenedor global."""
    ...
    return cls


class BasePlugin(ABC):
    """ Lógica común a todos los plugins.
    - Los plugins deben tener configuración interna.
    - Los plugins pueden ser habilitados o deshabilitados solamente usando los métodos enable y disable.
    """
    def __init__(self, **config: Any) -> None:
        ...

    @property
    def is_enabled(self):
        """Checkea si el plugin esta habilitado."""


    def enable(self):
	    """Marca el plugin como habilitado."""


    def disable(self):
	    """Marca el plugin como deshabilitado."""



    @abstractmethod
    def run(self) -> Any:
        """
        Ejecuta la lógica del plugin y devuelve un valor.
        Debe propagar PluginExecutionError si algo sale mal.
        """
        raise NotImplementedError


class PluginFactory(BasePlugin):
    """Factoría de plugins."""


    def is_enabled(self):
        pass





    @staticmethod
    def create(name: str, strict: bool = False, **config: Any) -> Optional[BasePlugin]:
        """
        Devuelve una instancia del plugin solicitado.

        - strict determina si se debe levantar una excepcion si el tipo de plugin no existe.
        """
        plugin_name = name

        return plugin_name





@plugin
class GreetingPlugin(BasePlugin):
    """Saluda a la persona indicada. Config esperado: user='...'. """

    def run(self) -> dict:
        """Retorna {'message': 'Hello, <user>'}."""
        # TODO: implementar lógica real
        ...


# Ejemplo de uso
plugin_inst = PluginFactory.create("GreetingPlugin", user="Ada", strict=True)
print(plugin_inst.run())          # → {'message': 'Hello, Ada!'}
plugin_inst.disable()
print("¿Habilitado?", plugin_inst.is_enabled)
