

import math

class MinHeap:
    def __init__(self):
        self.size = 0
        # We start with an arbitray element, 
        # bc we have trouble mapping children that start from index zero (index 1 is much easier to work with)
        self.heap = [0]  # Binary tree represented as a array

    def popMin(self):
        if self.size == 0:
            return 
        toReturn = self.heap[1] # first element is not 0, 0 is a dummy.

        # bring last value to top to resort the heap
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = math.inf
        self.size -= 1

        # will always start at the root
        self.swapDown(1)

        return toReturn


    def printHeap(self):
        for x in range(1, self.size + 1):
            print(self.heap[x])


    # always swap parent with the smaller child
    def swapDown(self, idx):

        if(idx >= self.size):
            return

        # Stop swapping when we have no more children OR if we are smaller than the children (handled by failing test cases below)
        if ((idx*2) > self.size) and ((idx*2 + 1) > self.size):
            return

        # There must be at least one child left
        child1 = math.inf
        child2 = math.inf

        if (idx*2) <= self.size:
            child1 = self.heap[idx*2]
        if ( (idx*2) + 1 ) <= self.size:
            child2 = self.heap[(idx*2) + 1]
        
        # if the parent is > than one of the children find the smaller and swap
        if (self.heap[idx] > child1) or (self.heap[idx] > child2):
            #swap with the smaller child
            if child1 < child2:
                self.heap[idx], self.heap[idx*2] = self.heap[idx*2], self.heap[idx]
                self.swapDown(idx*2)
            else:
                self.heap[idx], self.heap[(idx*2) + 1] = self.heap[(idx*2) + 1], self.heap[idx]
                self.swapDown((idx*2) + 1)

        # The parent is smaller (=<) than both the children
        else:
            return


        



    # if a child is greater than a parent, swap.
    # use the index itself
    def swapUp(self, idx):
        # base case
        if idx == 1:
            return
        
        idxValue = self.heap[idx]
        # will always trucate twoards zero
        parentIdx = int( idx / 2 )
        parentVal = self.heap[ parentIdx ]
        if int(parentVal > idxValue):
            self.heap[idx], self.heap[parentIdx] = self.heap[parentIdx], self.heap[idx]
            self.swapUp(parentIdx) 

    def insert(self, x):
        
        #might be broken
        if self.heap[len(self.heap) - 1] == math.inf:
            self.heap[self.size + 1] = x
        else:
            self.heap.append(x)

        self.size += 1
        
        # check if we need to swap
        self.swapUp(self.size)




if __name__ == "__main__":

    mh = MinHeap()

    for x in range(5, 0, -1):
        mh.insert(x)

    # print("original")
    # mh.printHeap()

    mh.popMin()
    mh.popMin()
    mh.popMin()
    mh.popMin()
    mh.popMin()
    mh.popMin()
    mh.popMin()

    mh.insert(18)
    mh.insert(21)
    mh.insert(7)
    mh.insert(57)
    mh.insert(12)
    
    # print("after pop")
    mh.printHeap()

    pass


        