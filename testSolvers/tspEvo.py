import random


class GeneticOperations():
	def __init__(self):

		self.params = {
			'populationSize': 20,
			'tournamentNumber': 3,
			'generationNumber': 20
		}
	def distance(self, p1, p2):
		d = (((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**.5
		return int(d)



	def tournamentSelection(self, population):
		selectedIndividuals = random.sample(population, self.params['tournamentNumber'])
		self.fitnessEvaluation(selectedIndividuals)



	def fitnessEvaluation(self, selectedIndividuals):
		fitnessLink = {}
		fitnessRanked = []

		print(selectedIndividuals,end='\n\n')
		for index, candidiate in enumerate(selectedIndividuals):
			pos = 0
			travelCost = 0
			while pos != len(candidiate)-1:
				p1 = Nodes[str(candidiate[pos])]
				p2 = Nodes[str(candidiate[pos+1])]
				travelCost += self.distance(p2, p1)
				pos += 1

			fitnessLink[str(travelCost)] = candidiate


		fitnessRanked = sorted(fitnessLink)
		mate = (fitnessLink[fitnessRanked[0]], fitnessLink[fitnessRanked[1]])

		print(fitnessLink)
		print(fitnessRanked)
		print(mate)
		print('\n')







	def mutation(self):
		pass

	def crossover(self):
		pass



def generatePopulation(size,eleSize):
	P = []
	lang = tuple([ x for x in range(2,eleSize+1) ]) #generating nodes
	for candidiate in range(0, size):
		chromosome = []
		poss = list(lang)
		while len(poss) != 0:
			selected = random.choice(poss)
			del poss[poss.index(selected)]
			chromosome.append(selected)
		P.append(chromosome)

	return P



def Evolution(population, params):

	for x in range(0, 1):


		for x in range(0, int(params['populationSize']/2)):
			selected = G.tournamentSelection(population)



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
