import math
class GraphNode:
    def __init__(self, name, num):
        super().__init__()
        self.name = name
        self.num = num
        visited = False
        self.effort = math.inf
        self.path = []

    def __lt__(self, other):
        if(self.effort < other.effort):
            return True
        else:
            return False
