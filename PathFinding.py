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

class AStar:
    
    """As a constructior it takes a 2D array with 0's where the robot can go and 1's where it cant"""
    def __init__(self, arrayMap, bounds):
        self.bounds = bounds
        self.array = arrayMap
    """Returns a list (reverse order) or the nodes to go to in orger to get to the obective, or false if its imposible. Takes 2 nodes, starting position and end position. """
    def AStar(self, start, goal):
        matrix = self.array
        closedSet = []

        openSet = [start]

        cameFrom = {}

        gScore = {}
        gScore[start] = 0

        fScore = {}
        fScore[start] = self.heuristic_cost_estimate(start, goal)

        KeepLooping = True
        while KeepLooping :

            current = self.lowestValueInDict(openSet, fScore)
            if current.x == goal.x and current.y == goal.y:
                return self.reconstruct_path(cameFrom, goal)
            openSet.remove(current)
            closedSet.append(current)

            neighbors = []
            if current.x > 0:
                if matrix[current.x -1][current.y] == 0:
                    neighbors.append(node(current.x -1, current.y))
            if current.y > 0:
                if matrix[current.x][current.y - 1] == 0:
                    neighbors.append(node(current.x, current.y - 1))

            if current.x != self.bounds - 1:
                if matrix[current.x + 1][current.y] == 0:
                        neighbors.append(node(current.x + 1, current.y))

            if current.y != self.bounds - 1:
                if matrix[current.x][current.y + 1] == 0:
                        neighbors.append(node(current.x, current.y + 1))
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
                fScore[neighbor] = gScore[neighbor] + self.heuristicCostEstimate(neighbor, goal)
            if openSet == []:
                KeepLooping = False
        return False

    #takes a node:start positon, items an array of nodes
	#returns 2 items: chosen goal, path toget there (out put from AStar(...))
    def closestNode(self, start, goals):
        lowestGoal = None
        lowestPath = ""
        for goal in goals:
            path = self.AStar(start, goal)
            if lowestGoal is None or len(path) < len(lowestPath) :
                lowestGoal = goal
                lowestPath = path

        return lowestGoal, lowestPath


    def heuristicCostEstimate(self, start, end):
        #this should work but should idealy be the minimum posible path
        x = start.x - end.x
        y = start.y - end.y
        if x < 0:
            x = x * -1
        if y < 0:
            y = y * -1
        return x + y

    def contains(self, array, val):
        for x in array:
            if x == val:
                return True
        return False

    def lowestValueInDict(self, openSet, dic):
        lowestVal = None
        lowestKey = ""

        for value in openSet:
            score = dic[value]
            if lowestVal == None or score < lowestVal:
                lowestKey = value
                lowestVal = score
        return lowestKey

    def reconstructPath(self, cameFrom, current):
        total_path = [current]
        while current in cameFrom:
            current = cameFrom[current]
            total_path.append(current)
        return total_path

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

    Path = PathFind(array(5), 5)

    goal, path = Path.ClosestNode(node(0,0), [node(2,2), node(3,1)])
    print(goal)
    for point in path:
        print(point.x, point.y)
    Path = PathFind(array(5), 5)
    path = Path.AStar(node(0,0), node(4,3))
    for point in path:
        #print(point.x, point.y)
        pass
