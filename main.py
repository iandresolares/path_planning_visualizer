# * Custom imports
from path_planners.bug import BugPlanner
from path_planners.simple_planner import SimplePlanner
from grid import Grid
from common import CellType


if __name__ == "__main__":
    SIZE = 50
    PATH_SIZE = 20

    grid = Grid(SIZE)
    grid.generate_obstacles()
    start_cell = grid.generate_cell(CellType.START)
    goal_cell = grid.generate_cell(CellType.GOAL)
    print(f"START: {start_cell}")
    print(f"GOAL: {goal_cell}")
    planner = SimplePlanner(start_cell, goal_cell, path_size=PATH_SIZE, grid=grid)
    # planner = BugPlanner(
    #     start=start_cell, goal=goal_cell, path_size=PATH_SIZE, grid=grid
    # )
    planner.calculate_path()
    grid.display(display_path=planner.display_path)
