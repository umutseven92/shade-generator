from dataclasses import dataclass


@dataclass
class Color:
    """Representation of an RGBA color."""
    r: float
    g: float
    b: float
    a: float
