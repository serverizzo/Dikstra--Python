import math
class graphNode2:

    def __init__(self):
        self.num  = 0 
        self.weight = math.inf
        self.path = []

    def setNum(self, x):
        self.num = x
    
    def getNum(self):
        return self.num

    # I don't think we will need this
    # def setPath(self, givenPath):
    #     # copy given path
    #     self.path = givenPath
    #     # add yourself to the list  
    #     self.path.append(self.getNum())

    # def erasePath(self):
    #     self.path = []

    def setWeight(self, x):
        self.weight = x

    def getWeight(self):
        return self.weight

    def __gt__(self, other):
        if other == math.inf:
            return False
        
        if self.weight > other.weight:
            return True
        else:
            return False

    def __lt__(self, other):
        
        # if we compare against infinity, other.weight would throw an error.
        if other == math.inf:
            return True

        if self.weight < other.weight:
            return True
        else:
            return False


if __name__ == "__main__":
    
    x = graphNode2()
    x.setWeight(5)
    y = graphNode2()
    y.setWeight(50)
    # print(y < x)
    
    
    pass