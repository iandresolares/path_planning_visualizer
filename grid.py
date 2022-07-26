from matplotlib import colors
from matplotlib.colors import ListedColormap
import random
from typing import Callable
from matplotlib import pyplot

# * Custom imports
from common import CellType


class Grid:
    def __init__(self, size: int):
        self.size = size
        self.matrix = [[0 for _ in range(0, self.size)] for _ in range(0, self.size)]
        self.obstacle_base_probability = 0.2
        self.obstacle_next_probablity = 0.1
        self.cell_posibilites = [CellType.EMPTY, CellType.OBSTACLE]
        self.color_map = ListedColormap(["white", "black", "lightblue", "red"])

    def check_border(self, row_index, col_index):
        return (
            row_index == 0
            or row_index == self.size - 1
            or col_index == 0
            or col_index == self.size - 1
        )

    def display(self, display_path: Callable):
        colors.Normalize(vmin=0, vmax=len(CellType) - 1)
        pyplot.figure(figsize=(10, 10))
        pyplot.imshow(self.matrix, cmap=self.color_map, origin="lower")
        # * PATH
        display_path()
        # *
        pyplot.show()

    def calculate_obstacle_probability(self, row_index, col_index):
        total_probability = self.obstacle_base_probability
        if self.matrix[row_index - 1] == CellType.OBSTACLE:
            total_probability += self.obstacle_next_probablity
        if self.matrix[row_index + 1] == CellType.OBSTACLE:
            total_probability += self.obstacle_next_probablity
        if self.matrix[col_index - 1] == CellType.OBSTACLE:
            total_probability += self.obstacle_next_probablity
        if self.matrix[col_index + 1] == CellType.OBSTACLE:
            total_probability += self.obstacle_next_probablity
        return total_probability

    def generate_obstacles(self):
        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                if self.check_border(i, j):
                    self.matrix[i][j] = float(
                        random.choices(
                            self.cell_posibilites,
                            weights=[
                                1 - self.obstacle_base_probability,
                                self.obstacle_base_probability,
                            ],
                        )[0]
                    )
                    continue
                obs_prob = self.calculate_obstacle_probability(i, j)
                self.matrix[i][j] = float(
                    random.choices(
                        self.cell_posibilites,
                        weights=[
                            1 - obs_prob,
                            obs_prob,
                        ],
                    )[0]
                )

    def generate_cell(self, cell_type: CellType):
        while True:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.check_free_neighbour(row, col):
                self.matrix[row][col] = cell_type
                return col, row

    def up_cell(self, row, col):
        if row == 0:
            return None
        return self.matrix[row - 1][col]

    def bottom_cell(self, row, col):
        if row == self.size - 1:
            return None
        return self.matrix[row + 1][col]

    def left_cell(self, row, col):
        if col == 0:
            return None
        return self.matrix[row][col - 1]

    def right_cell(self, row, col):
        if col == self.size - 1:
            return None
        return self.matrix[row][col + 1]

    def check_free_neighbour(self, row, col):
        neighbours = [
            self.up_cell(row, col),
            self.bottom_cell(row, col),
            self.left_cell(row, col),
            self.right_cell(row, col),
        ]
        if CellType.EMPTY in neighbours:
            return True
        return False
