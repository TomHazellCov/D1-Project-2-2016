from math import *
class Node:
    """Class used to store an X and Y cordanat"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        #to test if an x and y cord are equal
        return self.__dict__ == other.__dict__

    def __hash__(self):
        #required for this to be added to dictionery
        return hash(tuple((self.x, self.y)))

    def __str__(self):
        return str(self.x) + " " + str(self.y)

class Pathfinding:

    """As a constructior it takes a 2D array with 0's where the robot can go and 1's where it cant"""
    def __init__(self, arrayMap):
        self.array = arrayMap
    """Returns a list (reverse order) or the nodes to go to in orger to get to the obective, or false if its imposible. Takes 2 nodes, starting position and end position. """
    def astar(self, start, goal):
        matrix = self.array
        #TODO fix this:
        bounds_y = len(matrix[0])
        bounds_x = len(matrix)
        closedSet = []

        openSet = [start]

        cameFrom = {}

        gScore = {}
        gScore[start] = 0

        fScore = {}
        fScore[start] = self.heuristic_cost_estimate(start, goal)

        KeepLooping = True
        while KeepLooping :

            current = self.lowest_value_in_dict(openSet, fScore)
            if current.x == goal.x and current.y == goal.y:
                return self.reconstruct_path(cameFrom, goal)
            openSet.remove(current)
            closedSet.append(current)

            # gets node neighbours 
            neighbors = []
            if current.x > 0:
                if matrix[current.x -1][current.y] == 0:
                    neighbors.append(Node(current.x -1, current.y))
            if current.y > 0:
                if matrix[current.x][current.y - 1] == 0:
                    neighbors.append(Node(current.x, current.y - 1))
            if current.x != bounds_x - 1:
                if matrix[current.x + 1][current.y] == 0:
                        neighbors.append(Node(current.x + 1, current.y))
            if current.y != bounds_y - 1:
                if matrix[current.x][current.y + 1] == 0:
                        neighbors.append(Node(current.x, current.y + 1))
            
            for neighbor in neighbors:
                if self.contains(closedSet, neighbor):
                    continue

                tentative_gScore = gScore[current] + 1#1 being distance betwen nodes

                if not self.contains(openSet, neighbor):
                    openSet.append(neighbor)
                elif tentative_gScore >= gScore[neighbor]:
                    continue
                #if it got here that measn it is the best posible route
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + self.heuristic_cost_estimate(neighbor, goal)
            if openSet == []:
                KeepLooping = False

        return False

    #takes a node:start positon, items an array of nodes
    #returns 2 items: chosen goal, path to get there (out put from AStar(...))
    def closest_node(self, start, goals):
        lowestGoal = None
        lowestPath = ""
        for goal in goals:
            path = self.astar(start, goal)
            if lowestGoal is None or len(path) < len(lowestPath) :
                lowestGoal = goal
                lowestPath = path

        return lowestGoal, lowestPath


    def heuristic_cost_estimate(self, start, end):
        #this should work but should idealy be the minimum posible path
        x = abs(start.x - end.x)
        y = abs(start.y - end.y)

        return sqrt(x*x + y*y)

    def contains(self, array, val):
        for x in array:
            if x == val:
                return True
        return False

    def lowest_value_in_dict(self, openSet, dic):
        lowestVal = None
        lowestKey = ""

        for value in openSet:
            score = dic[value]
            if lowestVal == None or score < lowestVal:
                lowestKey = value
                lowestVal = score
        return lowestKey

    def reconstruct_path(self, cameFrom, current):
        total_path = [current]
        while current in cameFrom:
            current = cameFrom[current]
            total_path.append(current)

        return reversed(total_path)

def array(bounds):
    #make 5x5 array of 0's
    Matrix = [[0 for x in range(bounds)] for x in range(bounds)]
    #add random objects
    Matrix[0][3] = 1
    Matrix[1][2] = 1
    Matrix[4][4] = 1
    Matrix[2][3] = 1
    return Matrix

if __name__ == '__main__':

    Path = Pathfinding(array(5), 5)

    goal, path = Path.ClosestNode(Node(0,0), [Node(2,2), Node(3,1)])
    print(goal)
    for point in path:
        print(point.x, point.y)
    pathfinding = Pathfinding(array(5), 5)
    path = Path.astar(Node(0,0), Node(4,3))
    for point in path:
        #print(point.x, point.y)
        pass
