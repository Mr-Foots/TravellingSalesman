import random


class GeneticOperations():
	def __init__(self):

		self.params = {
			'populationSize': 20,
			'tournamentNumber': 3,
			'generationNumber': 1,
			'mutationRate': .01
		}
	def distance(self, p1, p2):
		#calculates distance from two points
		d = (((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**.5
		return int(d)



	def tournamentSelection(self, population):
		fitnessLink = {}
		#randomly selects n number of candidates from the population
		selectedIndividuals = random.sample(population, self.params['tournamentNumber'])

		for indvidulal in selectedIndividuals:
			fitnessLink[str(self.fitnessEvaluation(individual))] = individual

		#to find the sequences with the lowest travel time, the fitness values are sorted and matched aganist the orginal dictionary
		fitnessOrdered = sorted(map(int, fitnessLink.keys()))
		matingPair = (fitnessLink[str(fitnessRanked[0])], fitnessLink[str(fitnessRanked[1])])
		
		return mates


	def fitnessEvaluation(self, individual):
		travelCost = 0


		#loop will go through each node and calculate the distance between the two of them
		for i in range(1, len(individual)):
			p1 = Nodes[str(candidiate[i-1])]
			p2 = Nodes[str(candidiate[i])]
			travelCost += self.distance(p2, p1) #distance formula

		return travelCost



	def crossover(self):
		pass



	#NEEDS TO BE TESTED
	def mutation(self, candidiate):
		point1, point2 = ''

		r = random.randint(1,100)
		r = r/100

		if r == self.params.mutationRate:
			while point1 == point2:
				point1 = random.choice(candidate)
				point2 = random.choice(candidate)

			candidate[candidate.index(point1)] = point2
			candidate[candidate.index(point2)] = point1
			return candidate
		else:
			return candidate

#Function will create initial Population. Size is length of pop, eleSize is length of TSP
def generatePopulation(size,eleSize):

	P = [] #holds population
	lang = tuple([ x for x in range(2,eleSize+1) ]) #generating matching node names

	#Loop creates the n number of candidates
	for candidiate in range(0, size):

		chromosome = []
		poss = list(lang)

		#loops to create visiting sequence
		while len(poss) != 0:

			selected = random.choice(poss) #randomly chooses a possible node
			del poss[poss.index(selected)] #deletes that node so it doesnt repeat
			chromosome.append(selected)
		P.append(chromosome)

	return P


#Controlling Evolution function. Actual generation iteration happens here
def Evolution(population, params):

	#TERMINATION CONDITION GOES HERE
	for x in range(0, generationNumber):
		newPopulation = []
		mates = []

		#run for half the population. Each mate pair will make two children
		for x in range(0, int(params['populationSize']/2)):
			selected = G.tournamentSelection(population)
			mates = G.fitnessEvaluation(selected)
			children = G.crossover(mates)
			newPopulation.extend(children)

		for candidate in newPopulation:
			#Attempts to mutate. If mutation does not occur then return candidate back to population to restart cycle
			population.append(mutate(candidate, newPopulation))



def main():
	global G
	global Nodes

	Nodes = {
		'1': (565.0, 575.0),
		'2': (25.0, 185.0),
		'3': (345.0, 750.0),
		'4': (945.0, 685.0),
		'5': (845.0, 655.0),
		'6': (880.0, 660.0),
		'7': (25.0, 230.0),
		'8': (525.0, 1000.0),
		'9': (580.0, 1175.0),
		'10': (650.0, 1130.0),
		'11': (1605.0, 620.0),
		'12': (1220.0, 580.0),
		'13': (1465.0, 200.0),
		'14': (1530.0, 5.0),
		'15': (845.0, 680.0)
	}


	G = GeneticOperations()


	population = generatePopulation(G.params['populationSize'], len(Nodes))
	Evolution(population, G.params)
