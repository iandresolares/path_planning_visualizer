from path_planners.path_planner_interface import PathPlannerInterface


class SimplePlanner(PathPlannerInterface):
    def calculate_path(self):
        current = self.start
        cont = 0
        while current != self.goal:
            cont += 1
            if cont == 1000:
                return
            if self.goal[0] > current[0]:
                current = (current[0] + 1, current[1])
                self.path.append(current)
            elif self.goal[0] < current[0]:
                current = (current[0] - 1, current[1])
                self.path.append(current)
            if self.goal[1] > current[1]:
                current = (current[0], current[1] + 1)
                self.path.append(current)
            elif self.goal[1] < current[1]:
                current = (current[0], current[1] - 1)
                self.path.append(current)
            print(current)
