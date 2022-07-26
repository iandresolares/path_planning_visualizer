from functools import partial

# * Custom imports
from path_planners.path_planner_interface import PathPlannerInterface
from common import Cell, Direction, CellType


class BugPlanner(PathPlannerInterface):
    def calculate_path(self):
        args = []
        cell_dict = {
            Direction.BOTTOM: partial(self.grid.bottom_cell, *args),
            Direction.TOP: partial(self.grid.top_cell, *args),
            Direction.RIGHT: partial(self.grid.right_cell, *args),
            Direction.LEFT: partial(self.grid.left_cell, *args),
        }
        current = self.start

        # TODO check if the cell is empty, if it is not, check the other direction
        # TODO if is not either, raise an exception
        # TODO if it is move to that cell (add it to the path) and continue the loop

        while current != self.goal:
            goal_direction = self.calculate_goal_direction(current)
            if cell_dict[goal_direction.x](current):
                pass

    def calculate_goal_direction(
        self, current_position: Cell
    ) -> tuple[Direction, Direction]:

        if self.goal.x > current_position.x:
            x_dir = Direction.RIGHT
        elif self.goal.x < current_position.x:
            x_dir = Direction.LEFT
        else:
            x_dir = None

        if self.goal.y > current_position.y:
            y_dir = Direction.TOP
        elif self.goal.y < current_position.y:
            y_dir = Direction.BOTTOM
        else:
            y_dir = None

        return x_dir, y_dir
