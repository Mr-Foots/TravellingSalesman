import random
import string

class Node:
    def __init__(self):
        self.name = ''
        self.coords = ()
        self.marked = False
    def setParams(self, coords, name):
        self.name = name
        self.coords = coords

    def setMarked(self, marked):
        self.marked = marked

def createGraph(n=6, maxX=15, maxY=15):
    alphabet = string.ascii_uppercase
    nodes = []

    for i in range(0, n):
        temp = Node()

        xCoord = random.randint(0, maxX)
        yCoord = random.randint(0, maxY)
        name = alphabet[i]
        temp.setParams((xCoord, yCoord), name)

        nodes.append(temp)
    return nodes


class Graph:
    def __init__(self):
        self.graph = createGraph()
        
    def findDistance(self, node1, node2):
        xDiff = node2.coords[0] - node1.coords[0]
        yDiff = node2.coords[1] - node1.coords[1]
        sumSquares = (xDiff**2) + (yDiff**2)
        distance = int(sumSquares**.5)

        return distance