class node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.isObject = isObject
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple((self.x, self.y)))

class PathFind:

    def __init__(self):
        self.bounds = 5

    def A(self, start, goal):

        matrix = self.array()
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
            print(current, "cur")
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
                fScore[neighbor] = gScore[neighbor] + self.heuristic_cost_estimate(neighbor, goal)
            if openSet == []:
                KeepLooping = False 
        return False
            
            

    def heuristic_cost_estimate(self, start, end):
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
        lowestVal = 9999999999999999
        lowestKey = ""

        for value in openSet:
            score = dic[value]
            if score < lowestVal:
                lowestKey = value
                lowestVal = score
                print(lowestKey.x, lowestKey.y)
        return lowestKey

    def reconstruct_path(self, cameFrom, current):
        total_path = [current]
        while current in cameFrom:
            current = cameFrom[current]
            total_path.append(current)
        return total_path
            


    def array(self):
        #make 5x5 array of 0's
        Matrix = [[0 for x in range(self.bounds)] for x in range(self.bounds)] 
        #add random objects
        Matrix[0][3] = 1
        Matrix[1][2] = 1
        Matrix[4][4] = 1
        Matrix[2][3] = 1
        return Matrix
    




Path = PathFind()
path = Path.A(node(0,0), node(4,3))
for point in path:
    print(point.x, point.y)
