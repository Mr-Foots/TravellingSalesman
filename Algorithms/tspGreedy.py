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
