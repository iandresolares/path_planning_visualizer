from matplotlib import colors
from matplotlib.colors import ListedColormap
import random
from typing import Callable
from matplotlib import pyplot
import pandas as pd

# * Custom imports
from common import CellType, Cell


class Grid:
    def __init__(self, size: int):
        self.size = size
        # self.matrix = [[0 for _ in range(0, self.size)] for _ in range(0, self.size)]
        self.matrix = pd.DataFrame(
            [[0 for _ in range(0, self.size)] for _ in range(0, self.size)],
            index=[i for i in range(self.size - 1, -1, -1)],
        )
        self.obstacle_base_probability = 0.05
        self.obstacle_next_probablity = 0.4
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
        if self.matrix[row_index - 1][col_index] == CellType.OBSTACLE:
            total_probability += self.obstacle_next_probablity
        if self.matrix[row_index + 1][col_index] == CellType.OBSTACLE:
            total_probability += self.obstacle_next_probablity
        if self.matrix[row_index][col_index - 1] == CellType.OBSTACLE:
            total_probability += self.obstacle_next_probablity
        if self.matrix[row_index][col_index + 1] == CellType.OBSTACLE:
            total_probability += self.obstacle_next_probablity
        return total_probability

    # def generate_obstacles(self):
    #     for i, row in enumerate(self.matrix):
    #         for j, _ in enumerate(row):
    #             if self.check_border(i, j):
    #                 self.matrix[i][j] = float(
    #                     random.choices(
    #                         self.cell_posibilites,
    #                         weights=[
    #                             1 - self.obstacle_base_probability,
    #                             self.obstacle_base_probability,
    #                         ],
    #                     )[0]
    #                 )
    #                 continue
    #             obs_prob = self.calculate_obstacle_probability(i, j)
    #             self.matrix[i][j] = float(
    #                 random.choices(
    #                     self.cell_posibilites,
    #                     weights=[
    #                         1 - obs_prob,
    #                         obs_prob,
    #                     ],
    #                 )[0]
    #             )

    def generate_obstacles(self):
        for i in range(self.size):
            for j in range(self.size):
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

    def generate_cell(self, cell_type: CellType) -> Cell:
        while True:
            cell = Cell(
                x=random.randint(0, self.size - 1),
                y=random.randint(0, self.size - 1),
            )
            if self.check_free_neighbour(cell):
                self.matrix[cell.x][cell.y] = cell_type
                return cell

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

    def check_free_neighbour(self, current_cell: Cell):
        neighbours = [
            self.up_cell(current_cell.x, current_cell.y),
            self.bottom_cell(current_cell.x, current_cell.y),
            self.left_cell(current_cell.x, current_cell.y),
            self.right_cell(current_cell.x, current_cell.y),
        ]
        if CellType.EMPTY in neighbours:
            return True
        return False
