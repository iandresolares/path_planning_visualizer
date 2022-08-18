from path_planners.path_planner_interface import PathPlannerInterface
from common import Direction


class SimplePlanner(PathPlannerInterface):
    def calculate_path(self):
        current = self.start
        print(current)
        while current != self.goal:
            if self.goal.x > current.x:
                current.x, current.y = (current.x + 1, current.y)
                self.path.append((current.x, current.y))
            elif self.goal.x < current.x:
                current.x, current.y = (current.x - 1, current.y)
                self.path.append((current.x, current.y))
            if self.goal.y > current.y:
                current.x, current.y = (current.x, current.y + 1)
                self.path.append((current.x, current.y))
            elif self.goal.y < current.y:
                current.x, current.y = (current.x, current.y - 1)
                self.path.append((current.x, current.y))
            print(current)

    # def calculate_path(self):
    #     current = self.start

    #     while current != self.goal:
    #         for direction in Direction:
    #             pass

    # def calculate_goal_direction(self, current_cell):
    #     res = self.goal - current_cell
    #     if res
