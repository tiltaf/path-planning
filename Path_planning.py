class A*:
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
                    cost = cost + 2*self.map_grid[x2][y2]*neig[2+i][2+j]
        return cost

    def path_find():
        '''function to populate the possible path and find best path

        Args:
            None
        return:
            best path between given two points'''
        def get_optimum():
            x = goal[0]
            y = goal[1]
            policy[x][y] = 5
            expand[x][y] = -50
            print(action[x][y])
            while x != init[0] or y != init[1]:
                  x2 = x - delta[action[x][y]][0]
                  y2 = y - delta[action[x][y]][1]
                  expand[x2][y2] = 500
                  policy[x][y] = action[x][y]
                  x = x2
                  y = y2
                  path.append([x,y])
        path = []
        closed = [[0 for row in range(len(self.map_grid[0]))] for col in range(len(self.map_grid))]
        closed[init[0]][init[1]] = 1
        expand = [[-1 for row in range(len(self.map_grid[0]))] for col in range(len(self.map_grid)) ]
        action = [[-1 for row in range(len(self.map_grid[0]))] for col in range(len(self.map_grid))]
        policy = [[-1 for row in range(len(self.map_grid[0]))] for col in range(len(self.map_grid))]
        x = init[0]
        y = init[1]
        g = 0
        h = heuristic(x,y) + neighCost(x,y)
        f = g + h
        open = [[f, g, h, x, y]]
        found = False # flag that is set when search is complete
        resign = False # flag set if we can't find expand
        count = 0

        while not found and not resign:
            if len(open) == 0:
                        resign = True
                        print('resign')
            else:
                open.sort()
                open.reverse()
                next = open.pop()
                x = next[3]
                y = next[4]
                g = next[1]
                expand[x][y] = count
                count += 1
            if x == goal[0] and y == goal[1]:
                        found = True
#                        print('found yar')
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(self.map_grid) and y2 >=0 and y2 <len(self.map_grid[0]):
                        if closed[x2][y2] == 0 and self.map_grid[x2][y2] == 0:
                            g2 = g + cost
                            h2 = heuristic(x2,y2) + neighCost(x2,y2)
                            f2 = g2 + h2
                            open.append([f2, g2, h2, x2, y2])
                            closed[x2][y2] = 1
                            action[x2][y2] = i


        return path
