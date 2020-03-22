from MinHeap import MinHeap
from graphNode2 import graphNode2
import math

class dikstra:

    def __init__(self):
        x = math.inf
        # edge list
        self.el = [
            [x, 5, 8],
            [x, x, 1],
            [x, x, x]
        ]

        self.alreadyVisited = set()
        self.toVisit = MinHeap()
        self.cost = [x, x, x]

    def solve(self, s):

        source = graphNode2()
        source.setWeight(0)
        source.setNum(s)
        # set the source to 0
        self.cost[s] = 0
        # add source to the places to visit
        self.toVisit.insert(source)
        while not self.toVisit.isEmpty():
            # pop the next node
            curr = self.toVisit.popMin()
            # add Node to the alreadyVisited Set
            self.alreadyVisited.add(curr)
            # for each node in its list,
            for x in range(0, len(self.el[curr.getNum()])):
                #if the cost of the current node + the edge is < the cost of the other node, we found a new shortest path.
                if self.cost[curr.getNum()] + self.el[curr.getNum()][x] < self.cost[x]:
                    # set the new cost
                    self.cost[x] = self.cost[curr.getNum()] + self.el[curr.getNum()][x]
                    # add node toVist Set
                    temp = graphNode2()
                    temp.setNum(x)
                    temp.setWeight(self.cost[x])
                    self.toVisit.insert(temp)

                    
        print(self.cost)
        #return cost matrix/print


if __name__ == "__main__":
    d = dikstra()
    d.solve(0)
    pass
