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

    def __call__(self):
        return self.x, self.y


class Direction(int, Enum):
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()
