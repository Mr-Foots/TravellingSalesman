def copyright_notice():
    """
    The MIT License (MIT)

    Copyright (c) 2015 Fernando Felix do Nascimento Junior

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    """


import json

class Graph:
    '''
    Graph of costs.
    '''
    def __init__(self, graph):
        if isinstance(graph, dict):
            self.graph = graph

    def cost(self, a, b):
        return self.graph[a][b]

    def edges(self, vertex):
        return self.graph[vertex]

    def path_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            cost += self.cost(path[i], path[i + 1])
        return cost

    def vertex(self, position):
        return self.vertices()[position]

    def vertices(self):
        return list(self.graph.keys())


class NearestNeighbour:

    def __init__(self, start, graph):
        '''
        Solution of shortest path problem using nearest neighbour algorithm
        '''
        self.start = start
        self.graph = graph
        self.followedRoute = []
        self.routeCost = 0

    def nearest_neighbour(self, origin, neighbours):
        '''
        Returns the nearest neighbour of a vertice origin
        '''
        lowest_cost = float('Inf')
        nearest = None

        for neighbour in neighbours:
            cost = self.graph.cost(origin, neighbour)
            if cost < lowest_cost:
                lowest_cost = cost
                nearest = neighbour

        return nearest

    def solve(self):
        '''
        Executes the algorithm
        '''
        missing = list(self.graph.vertices())  # towns to be visited
        currentTown = self.start
        self.followedRoute.append(currentTown)
        missing.remove(currentTown)

        while len(missing) > 0:
            closest = self.nearest_neighbour(currentTown, missing)
            self.followedRoute.append(closest)
            self.routeCost += self.graph.cost(currentTown, closest)
            currentTown = closest
            missing.remove(currentTown)  # remove visited town


        #self.followedRoute.append(self.start)
        #self.routeCost += self.graph.cost(currentTown, self.start)


def main(nodes):
    graph = Graph(nodes)
    solution = NearestNeighbour(1, graph)
    solution.solve()
    print(solution.routeCost)
    print(solution.followedRoute)
    return solution.routeCost
