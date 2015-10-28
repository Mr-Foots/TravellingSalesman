import random


class GeneticOperations():
	def __init__(self):

		self.params = {
			'populationSize': 20,
			'tournamentNumber': 3

		}


	def tournamentSelection(self, population):
		selectedIndividuals = random.sample(population, self.params['tournamentNumber'])
		print(selectedIndividuals)




	def fitnessEvaluation():
		pass

	def mutation():
		pass

	def crossover():
		pass



def generatePopulation(size,eleSize):
	P = []
	lang = tuple([ x for x in range(1,eleSize+1) ]) #generating nodes

	for candidiate in range(0, size):
		chromosome = []
		poss = lang
		while len(poss) != 0:
			selected = random.choice(poss)
			del poss[poss.index(selected)]
			chromosome.append(selected)
		P.append(chromosome)

	return P



def Evolution(population, params):

	while True:
		for x in range(0, params['populationSize']/2):
			selected = tournamentSelection(population)



def main(nodes):
	global G = GeneticOperations()


	population = generatePopulation(G.params,len(nodes))