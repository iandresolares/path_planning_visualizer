import yaml

# * Custom imports
from path_planners.bug import BugPlanner
from path_planners.bug2 import Bug2Planner
from path_planners.simple_planner import SimplePlanner
from grid import Grid
from common import CellType


# function which read a config.yaml file and prints its content
def read_config(file_path: str):
    with open(file_path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


if __name__ == "__main__":

    config = read_config("config/config.yaml")

    grid = Grid(grid_config=config["grid"])
    grid.generate_obstacles()
    start_cell = grid.generate_cell(CellType.START)
    goal_cell = grid.generate_cell(CellType.GOAL)
    print(f"START: {start_cell}")
    print(f"GOAL: {goal_cell}")
    # planner = SimplePlanner(start_cell, goal_cell, path_size=PATH_SIZE, grid=grid)
    planner = BugPlanner(
        planner_config=config["planner"],
        start=start_cell,
        goal=goal_cell,
        grid=grid,
    )
    # planner = Bug2Planner(
    #     start=start_cell, goal=goal_cell, path_size=PATH_SIZE, grid=grid
    # )
    planner.calculate_path()
    grid.display(display_path=planner.display_path)
