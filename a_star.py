import math

class AStar:
    def __init__(self, grid, start, end, distance):
        self.current = grid[start[0]][start[1]]
        self.openSet = [self.current]
        self.closedSet = []
        self.grid = grid
        self.end = grid[end[0]][end[1]]
        self.distance = distance
    
    def heuristic(self, p1, p2):
        if self.distance == 'manhattan':
            distance = sum(abs(a-b) for a,b in zip(p1.coords,p2.coords))
        else:
            # Euclidian distance
            distance = math.sqrt(((p1.row-p2.row)**2)+((p1.col-p2.col)**2))     
        return distance
    
    def check_next_field(self):
        o = self.openSet
        c = self.closedSet
        o_cords = [spot.coords for spot in o]
        c_cords = [spot.coords for spot in c]
        index = 0

        if len(o) == 0:
            print("No moves")
            return False

        for i in range(len(o)):
            if o[i].f < o[index].f:
                index = i
        current = o[index]
        current.is_current = True
        
        o.remove(current)
        c.append(current)

        for i in range(len(current.neighbours)):
            neighbour = current.neighbours[i]
            
            if neighbour.coords not in c_cords and neighbour.coords not in o_cords and not neighbour.is_wall: 
                o.append(neighbour)
                neighbour.g = current.g+1
                neighbour.considered = True
                neighbour.h = self.heuristic(neighbour, self.end)
                neighbour.f = neighbour.g + neighbour.h
                neighbour.previous = current
        
        if current.is_end:
            print("Path found")
            while current.previous:
                current.is_path = True
                current = current.previous
            return False
        return True
