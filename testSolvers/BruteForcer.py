import itertools


def distance(self, p1, p2):
		#calculates distance from two points
		d = (((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**.5
		return int(d)

def bruteForce(nodes):
	travelCosts = []


	originalSeq = range(1,len(nodes))
	sequences = list(itertools.permutations(originalSeq))
	
	for path in sequences:
		travelCost = 0
		for i in range(1,len(path)):
			travelCost += distance(nodes[str(i-1), str(i)])

		travelCost += distance(nodes[str(len(path)-1)], nodes[str(0)])
		travelCosts.append(travelCost)

	return sequences[travelCosts.index(min(travelCosts))]
