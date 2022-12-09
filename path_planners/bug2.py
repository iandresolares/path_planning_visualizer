import math

from .path_planner_interface import PathPlannerInterface
from common import Cell, Direction, CellType
from grid import Grid


class Bug2Planner(PathPlannerInterface):
    # def __init__(self, start: Cell, goal: Cell, path_size: int, grid: Grid):
    #     super().__init__(start, goal, path_size, grid)

    # def calculate_path(self):
    # stuck = False
    # current = self.start
    # while current != self.goal:
    # # * calculate goal direction
    # # *
    # goal_direction = self.get_goal_direction(current)

    # # * check if there is an obstacle in the goal direction
    # check_cell = get_next_cell(cell=current, direction=goal_direction)
    # if not self.check_obstacle(check_cell):
    # # * if there is no obstacle, move to that cell
    # current = check_cell
    # self.path.append((current.x, current.y))
    # else:
    # # * obstacles mode
    # done = False
    # while not stuck or done:
    # print("not stuck yet")
    # new_direction = get_obstacle_avoid_direction(
    # direction=goal_direction
    # )
    # if new_direction == goal_direction:
    # print("i'm stuck")
    # stuck = True
    # check_cell = get_next_cell(cell=current, direction=new_direction)
    # if not self.check_obstacle(cell=check_cell):
    # current = check_cell
    # self.path.append((current.x, current.y))
    # obstacle = True
    # while obstacle:
    # check_cell = get_next_cell(
    # current, direction=goal_direction
    # )
    # if not self.check_obstacle(cell=check_cell):
    # current = check_cell
    # self.path.append((current.x, current.y))
    # obstacle = False
    # else:
    # check_cell = get_next_cell(
    # current, direction=new_direction
    # )
    # if not self.check_obstacle(cell=check_cell):
    # current = check_cell
    # self.path.append((current.x, current.y))
    # else:
    # done = True
    # break
    # break

    # print("Current cell: ", current)

    def calculate_path(self):
        obstacle_following_mode = False
        current = self.start
        while current != self.goal:
            # * calculate goal direction
            # *
            goal_direction = self.get_goal_direction(current)

            # * check if there is an obstacle in the goal direction
            check_cell = get_next_cell(cell=current, direction=goal_direction)
            if not self.check_obstacle(check_cell):
                # * if there is no obstacle, move to that cell
                current = check_cell
                self.path.append((current.x, current.y))
            else:
                # * obstacle following mode
                obstacle_following_mode = True
                while obstacle_following_mode:
                    obstacle_avoidance_direction = get_obstacle_avoid_direction(
                        direction=goal_direction
                    )
                    check_cell = get_next_cell(
                        cell=current, direction=obstacle_avoidance_direction
                    )

    def get_goal_direction(self, current_cell: Cell) -> Direction:
        angle = math.degrees(
            math.atan2((self.goal.y - current_cell.y), (self.goal.x - current_cell.x))
        )
        if angle < 0:
            angle += 360
        # * First quadrant
        if angle > 0 and angle < 90:
            return Direction.TOP
        elif angle > 90 and angle < 180:
            return Direction.TOP
        elif angle > 180 and angle < 270:
            return Direction.BOTTOM
        elif angle > 270:
            return Direction.BOTTOM
        elif angle == 0:
            return Direction.RIGHT
        elif angle == 90:
            return Direction.TOP
        elif angle == 180:
            return Direction.LEFT
        elif angle == 270:
            return Direction.BOTTOM

    def check_obstacle(self, cell: Cell) -> bool:
        """True if there is an obstacle, false otherwise"""
        # ? In case it is None (an edge) return True as if there was an obstacle
        return self.grid.matrix[cell.x][cell.y] == CellType.OBSTACLE


def get_next_cell(cell: Cell, direction: Direction) -> Cell:
    if direction == Direction.RIGHT:
        return Cell(cell.x + 1, cell.y)
    elif direction == Direction.LEFT:
        return Cell(cell.x - 1, cell.y)
    elif direction == Direction.TOP:
        return Cell(cell.x, cell.y + 1)
    elif direction == Direction.BOTTOM:
        return Cell(cell.x, cell.y - 1)


def get_obstacle_avoid_direction(direction: Direction):
    if direction == Direction.RIGHT:
        return Direction.BOTTOM
    elif direction == Direction.BOTTOM:
        return Direction.LEFT
    elif direction == Direction.LEFT:
        return Direction.TOP
    elif direction == Direction.TOP:
        return Direction.RIGHT
