import math
import os

__all__ = ['readle', 'readbe', 'roundup', 'config_dir']


def readle(b: bytes) -> int:
    """Return little-endian bytes to an int."""
    return int.from_bytes(b, 'little')


def readbe(b: bytes) -> int:
    """Return big-endian bytes to an int."""
    return int.from_bytes(b, 'big')


def roundup(offset: int, alignment: int) -> int:
    """Round up a number to a provided alignment."""
    return int(math.ceil(offset / alignment) * alignment)


config_dir = os.path.expanduser('~') + '/.3ds'
