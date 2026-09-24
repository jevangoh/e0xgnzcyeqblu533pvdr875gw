from importlib.metadata import version, PackageNotFoundError
from .e0xgnzcyeqblu533pvdr875gw import e0xgnzcyeqblu533pvdr875gw as _

try:
    __version__ = version("e0xgnzcyeqblu533pvdr875gw")
except PackageNotFoundError:
    __version__ = "unknown"

__all__ = ["_", "__version__"]
