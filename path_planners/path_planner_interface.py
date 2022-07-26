from abc import ABC, abstractmethod
from matplotlib import pyplot

# * Custom modules
from grid import Grid


class PathPlannerInterface(ABC):
    def __init__(self, start, goal, path_size, grid: Grid):
        self.start = start
        self.goal = goal
        self.path_size = path_size
        self.path = []
        self.color_map = "Dark2"
        self.grid = grid

    def display_path(self):
        x = [c[0] for c in self.path]
        y = [c[1] for c in self.path]
        c = [i for i in range(len(self.path))]
        pyplot.scatter(x, y, s=self.path_size, c=c, cmap=self.color_map)

    @abstractmethod
    def calculate_path(self):
        ...
