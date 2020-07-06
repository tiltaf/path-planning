import numpy as np
import math
class Astar:
    '''A star path planning class to find optimal path given start point  and
    goal point in a map_grid using A* algorithm

    Attributes:
        map_grid(list of lists): representing the map pic/screenshot of any region
        startpoint(endpoints[0],list): containing x and y coordinates of startpoint for path planning
        goal(endpoints[0],list): containing x and y coordinates of endpoint/destination for path planning
        '''
    def __init__(self,map_grid,endpoints):
        self.map_grid = map_grid
        self.start_point = endpoints[0]
        self.goal = endpoints[1]
        self.step_cost = 2
        self.delta = [[-1, 0],  # go up
                 [0, -1],  # go left
                 [1, 0],  # go down
                 [0, 1]]  # go right
        self.neig = [[0.1, 0.25, 0.25, 0.25, 0.1],  # go up
                [0.25, 0.5, 0.5, 0.5, 0.25],  # go left
                [0.5, 0.5, 1, 0.5, 0.5],  # go down
                [0.25, 0.5, 0.5, 0.5, 0.25],
                [0.1, 0.25, 0.25, 0.25, 0.1]]
    def heuristic(self,x,y):
        '''function to give rough estimate cost of goal/destination point from given
        point using euclidean distance

        Args:
            x (int): x index of the point in map
            y (int): y index of the point in map
        return:
            euclidean distance(cost) of point(x,y) from goal point'''
        xdiff = self.goal[0] - x
        ydiff = self.goal[1] - y
        return math.sqrt(xdiff * xdiff + ydiff*ydiff)

    def neighCost(self,x,y):
        '''function penalize a potential path candidate point based on how much it is close
        to road border

        Args:
            x (int): x index of the point in map
            y (int): y index of the point in map
        return:
            cost (penalization) based on how close the point is to road border '''
        cost = 0.0
        for i in range(-2,2):
            x2 = x + i
            for j in range(-2,2):
                y2 = y + j
                if x2 >= 0 and x2 < len(self.map_grid) and y2 >=0 and y2 <len(self.map_grid[0]):
                    cost = cost + 2*self.map_grid[x2][y2]*self.neig[2+i][2+j]
        return cost

    def path_find(self):
        '''function to populate the possible path and find best path

        Args:
            None
        return:
            best path between given two points'''
        def get_optimum():
            x = self.goal[0]
            y = self.goal[1]
            expand[x][y] = -50
            print(action[x][y])
            while x != self.start_point[0] or y != self.start_point[1]:
                  x2 = x - self.delta[action[x][y]][0]
                  y2 = y - self.delta[action[x][y]][1]
                  expand[x2][y2] = 500
                  x = x2
                  y = y2
                  path.append([x,y])
        path = []
        closed_list = [[0 for row in range(len(self.map_grid[0]))] for col in range(len(self.map_grid))]
        closed_list[self.start_point[0]][self.start_point[1]] = 1
        expand = [[-1 for row in range(len(self.map_grid[0]))] for col in range(len(self.map_grid)) ]
        action = [[-1 for row in range(len(self.map_grid[0]))] for col in range(len(self.map_grid))]
        x = self.start_point[0]
        y = self.start_point[1]
        prev_cost = 0
        heuristic_cost = self.heuristic(x,y) + self.neighCost(x,y)
        updated_cost = prev_cost + heuristic_cost
        open_list = [[updated_cost, prev_cost, x, y]]
        found = False # flag that is set when search is complete
        resign = False # flag set if we can't find expand
        count = 0

        while not found and not resign:
            if len(open_list) == 0:
                        resign = True
                        print('resign')
            else:
                open_list.sort()
                open_list.reverse()
                next = open_list.pop()
                x = next[2]
                y = next[3]
                prev_cost = next[1]
                expand[x][y] = count
                count += 1
            if x == self.goal[0] and y == self.goal[1]:
                        found = True
#                        print('found yar')
            else:
                for i in range(len(self.delta)):
                    x2 = x + self.delta[i][0]
                    y2 = y + self.delta[i][1]
                    if x2 >= 0 and x2 < len(self.map_grid) and y2 >=0 and y2 <len(self.map_grid[0]):
                        if closed_list[x2][y2] == 0 and self.map_grid[x2][y2] == 0:
                            updated_cost = prev_cost + self.step_cost
                            heuristic_cost = self.heuristic(x2,y2) + self.neighCost(x2,y2)
                            total_cost = updated_cost + heuristic_cost
                            open_list.append([total_cost, updated_cost, x2, y2])
                            closed_list[x2][y2] = 1
                            action[x2][y2] = i
        get_optimum()

        return path
