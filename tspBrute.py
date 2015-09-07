import random

def create(n=6, maxX=15, maxY=15):
    cities = []
    #cities[0] will be origin point
    for i in range(0, n):
        xCoord = random.randint(0, maxX)
        yCoord = random.randint(0, maxY)

        cities.append((xCoord, yCoord))
