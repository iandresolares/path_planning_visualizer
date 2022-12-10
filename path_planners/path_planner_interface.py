from abc import ABC, abstractmethod
from matplotlib import pyplot

# * Custom modules
from grid import Grid
from common import Cell


class PathPlannerInterface(ABC):
    def __init__(self, planner_config: dict, start: Cell, goal: Cell, grid: Grid):
        self.start = start
        self.goal = goal
        self.path_size = planner_config["path_size"]
        self.path = []
        self.color_map = "Dark2"
        self.grid = grid

    def display_path(self):
        x = [cell[0] for cell in self.path]
        y = [self.grid.size - 1 - cell[1] for cell in self.path]
        c = [i for i in range(len(self.path))]
        pyplot.scatter(x, y, s=self.path_size, c=c, cmap=self.color_map)

    @abstractmethod
    def calculate_path(self):
        ...
