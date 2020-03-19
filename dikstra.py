from Graphnode import GraphNode
import math
import heapq

class Graph:
    # def __init__(self):
        
    edgeList = []
    nodeList = []
    alreadVisited = set()
    toVisit = [] # this will be our heap
    


    def addNode(self):
        if len(self.edgeList) == 0:
            self.edgeList.append([math.inf])
        else:
            z = len(self.edgeList) 
            for x in self.edgeList:
                x.append(math.inf)

            temp = [math.inf] * (z+1)
            self.edgeList.append(temp)
        self.nodeList.append(GraphNode("node " + str(len(self.edgeList)-1), len(self.edgeList)-1))

    def showNodeList(self):
        for x in self.nodeList:
            print(x.name)
    
    def showEdgeList(self):
        for x in self.edgeList:
            print(x)

    def showShortestPath(self):
        for i in self.nodeList:
            print(i.path)

    def addEdge(self, s, d, value):
        self.edgeList[s][d] = value
        self.edgeList[d][s] = value


    def dikstra(self, source, end):
        # source effor is always 0
        source.effort = 0
        # append source self to the its own path
        source.path = [source.name]

        # add source to heap
        self.toVisit.append(source)
        # while we have not already visited our end node
        while(end not in self.alreadVisited):
            # ensure that we are dealing with a min heap every time
            heapq.heapify(self.toVisit)
            curr = heapq.heappop(self.toVisit)
            # add node to already visited
            self.alreadVisited.add(curr)

            # for all nodes for which there is an edge (i.e. edges != inf) 
            for i in range(len(self.edgeList)):
                # Note: self.edgeList[curr.num] returns the array for all connections between the current node
                if self.edgeList[curr.num][i] == math.inf:
                    continue


                # if the other node has a effort > than effort of the current node + the edge between them
                if self.nodeList[i].effort > curr.effort + self.edgeList[curr.num][i]:
                    self.nodeList[i].effort = curr.effort + self.edgeList[curr.num][i]
                    # rewrite path 
                    self.nodeList[i].path = curr.path
                    self.nodeList[i].path.append(self.nodeList[i].name)


                add = True
                for x in self.toVisit:
                    if x == self.nodeList[i]:
                        add = False
                        break

                if add:
                    self.toVisit.append(self.nodeList[i])





g = Graph()
g.addNode()
g.addNode()
g.addNode()
g.addEdge(0,2,7)
g.addEdge(0,1,5)
g.addEdge(1,2,1)

g.showEdgeList()

g.dikstra(g.nodeList[0], g.nodeList[2])
g.showShortestPath()



print("Finished")