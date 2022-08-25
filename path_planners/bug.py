from functools import partial
import math


# * Custom imports
from path_planners.path_planner_interface import PathPlannerInterface
from common import Cell, Direction, CellType
from grid import Grid


class BugPlanner(PathPlannerInterface):
    def __init__(self, start: Cell, goal: Cell, path_size: int, grid: Grid):
        super().__init__(start, goal, path_size, grid)

    def calculate_path(self):
        current = self.start
        while current != self.goal:
            goal_direction = self.get_goal_direction(current)
            print(goal_direction)
            for direction in goal_direction:
                obstacle, cell = self.check_obstacle(current, direction)
                if not obstacle:
                    current = cell
                    self.path.append((current.x, current.y))
                    print(current)
                else:
                    # TODO !!!
                    pass

    def check_obstacle(self, cell: Cell, direction: Direction) -> bool:
        """Returns True if there is an obstacle"""
        x, y = cell.x, cell.y
        if direction == Direction.RIGHT:
            x += 1
        elif direction == Direction.TOP:
            y += 1
        elif direction == Direction.LEFT:
            x -= 1
        elif direction == Direction.BOTTOM:
            y -= 1
        return self.grid.matrix[x][y] == 1, Cell(x, y)

    def get_goal_direction(self, current_cell: Cell):
        angle = math.degrees(
            math.atan2((self.goal.y - current_cell.y), (self.goal.x - current_cell.x))
        )
        print(angle)
        # * First quadrant
        if angle > 0 and angle < 90:
            return [Direction.RIGHT, Direction.TOP]
        elif angle > 90 and angle < 180:
            return [Direction.TOP, Direction.LEFT]
        elif angle > 180 and angle < 270:
            return [Direction.LEFT, Direction.BOTTOM]
        elif angle > 270:
            return [Direction.BOTTOM, Direction.RIGHT]
        elif angle == 0:
            return [Direction.RIGHT]
        elif angle == 90:
            return [Direction.TOP]
        elif angle == 180:
            return Direction.LEFT
        elif angle == 270:
            return Direction.BOTTOM

    # def calculate_path(self):
    #     args = []
    #     cell_dict = {
    #         Direction.BOTTOM: partial(self.grid.bottom_cell, *args),
    #         Direction.TOP: partial(self.grid.top_cell, *args),
    #         Direction.RIGHT: partial(self.grid.right_cell, *args),
    #         Direction.LEFT: partial(self.grid.left_cell, *args),
    #     }
    #     current = self.start

    #     # TODO check if the cell is empty, if it is not, check the other direction
    #     # TODO if is not either, raise an exception
    #     # TODO if it is move to that cell (add it to the path) and continue the loop

    #     while current != self.goal:
    #         goal_direction = self.calculate_goal_direction(current)
    #         if cell_dict[goal_direction.x](current):
    #             pass

    # def calculate_goal_direction(
    #     self, current_position: Cell
    # ) -> tuple[Direction, Direction]:

    #     if self.goal.x > current_position.x:
    #         x_dir = Direction.RIGHT
    #     elif self.goal.x < current_position.x:
    #         x_dir = Direction.LEFT
    #     else:
    #         x_dir = None

    #     if self.goal.y > current_position.y:
    #         y_dir = Direction.TOP
    #     elif self.goal.y < current_position.y:
    #         y_dir = Direction.BOTTOM
    #     else:
    #         y_dir = None

    #     return x_dir, y_dir
