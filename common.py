from enum import Enum, auto
from dataclasses import dataclass


class CellType(int, Enum):
    EMPTY = 0
    OBSTACLE = 1
    START = 2
    GOAL = 3


@dataclass
class Cell:
    x: int
    y: int


class Direction(int, Enum):
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()
