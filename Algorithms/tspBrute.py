import itertools

def solve():
	minimum_distance = float('Inf')
	minimum_route = ''
	routes = itertools.permutations(range(2,len(Nodes)+1))
	for route in routes:
		distance = Nodes[1][route[0]] + sum(Nodes[route[i-1]][route[i]] for i in range(1, len(route)))

		if distance < minimum_distance:
			minimum_distance = distance
			minimum_route = route

	return distance, route


def main(nodes):
	global Nodes
	Nodes = nodes

	d,r = solve()
	print(d)
	print(r)
