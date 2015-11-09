import random
from collections import OrderedDict

class GeneticOperations():
	def __init__(self):
		self.params = {
			'populationSize': 30,
			'tournamentNumber': 3,
			'elitismRate': int(1/10),
			'eliteSurvivors': (populationSize * elitismRate),
			'generationNumber': 20,
			'mutationRate': (1,2,3,4,5)
		}
	def distance(self, p1, p2):
		#calculates distance from two points
		d = (((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**.5
		return int(d)



	def tournamentSelection(self, populationLinked):
		"""
			Function will select three chromosomes, then make the mating pair
			fitnessLink maps the sequence to the fitness Value for easy comparison and sorting
		"""

		fitnessLink = {}
		fitnessValues = []

		#randomly selects n number of chromosomes from the population. Sample is great because it cannot select repeats
		selectedChromosomes = random.sample(list(populationLinked), self.params['tournamentNumber'])

		[ fitnessValues.append(populationLinked[i]) for i in selectedChromosomes ]
		fitnessLink = dict(zip(list(map(str, fitnessValues)), selectedChromosomes))

		#to find the sequences with the lowest travel time, the fitness values are sorted and matched aganist the orginal dictionary
		fitnessOrdered = sorted(map(int, fitnessLink.keys()))
		matingPair = (fitnessLink[str(fitnessOrdered[0])], fitnessLink[str(fitnessOrdered[1])])

		return matingPair


	def fitnessEvaluation(self, chromosome):
		"""Takes an chromosome, returns the fitness value (travelCost) by summing the costs of each node"""

		travelCost = 0

		#loop will go through each node and calculate the distance between the two of them
		for i in range(1, len(chromosome)):
			p1 = Nodes[chromosome[i-1]]
			p2 = Nodes[chromosome[i]]
			travelCost += self.distance(p2, p1) #distance formula

		return travelCost



	def crossover(self, mates):
		"""
		Crossover will take mates, and will return one offspring.
		A splice is taken from the mother and inserted into offspring
		The nodes in the father are added to the offspring, if and only if, they do not
		appear in the splice. Offspring cannot have duplicates.

		"""

		mates = list(mates)
		random.shuffle(mates)#switching up who is mother and father a bit
		mother = list(mates[0])
		father = list(mates[1])
		offspring = [None] * len(mother)



		#setting start and endpoints for sequence to be crossed. Sorted makes sure its always
		#in least to greatest. Sample makes sure there are no duplicates
		points = sorted(random.sample(list(range(0,len(mother))), 2))
		start = points[0]
		end = points[1]

		spliced = mother[start:end]
		offspring[start:end] = spliced

		pointer = 0
		for index, slot in enumerate(offspring):
			if slot == None:
				gene = father[pointer]
				while gene in spliced:
					pointer +=1
					gene = father[pointer]

				offspring[index] = father[pointer]
				pointer += 1

		#print("Mother: ", mother)
		#print("Father: ", father)
		#print("Points: ", points)
		#print('Spliced: ', spliced)
		#print('Final Child: ', offspring)
		#print('\n\n')

		return ''.join(offspring)

	def mutation(self, chromosome):
		"""
			Mutation is vital to add genetic diversity
			a random number, r, is generated and if that matches the mutation rate then a swap mutation will occur
			a swap is necessary in order to produce a valid sequence
		"""
		r = random.randint(1,100)
		chromosome = list(chromosome)
		if r in self.params['mutationRate']:
			points = sorted(random.sample(list(range(0,len(chromosome))), 2))
			chromosome[points[0]], chromosome[points[1]] = chromosome[points[1]], chromosome[points[0]]
			return ''.join(chromosome)
		else:
			return ''.join(chromosome)

#Function will create initial Population. Size is length of pop, eleSize is length of TSP
def generatePopulation(pSize, instanceSize):
	"""
	Creates the initial population. 1 is the origin so it must be the first node
	"""

	P = [] #holds population
	F = []  #holds Fitness values
	lang = tuple([ x for x in range(2,instanceSize+1) ]) #generating the 'alphabet' for nodes

	#Loop creates the n number of chromosomes
	for chromosome in range(0, pSize):

		chromosome = []
		possible = list(lang)

		#loops to create visiting sequence
		while len(possible) != 0:
			selected = random.choice(possible) #randomly chooses a possible node
			del possible[possible.index(selected)] #deletes that node so it doesnt repeat
			chromosome.append(selected)

		chromosome.insert(0,1)
		chromosome = ''.join(chromosome)

		F.append(G.fitnessEvaluation(chromosome))
		P.append(chromosome)

	populationLinked = dict(zip(P,F))
	populationlinked = OrderedDict(sorted(populationlinked.items(), key=lambda t: t[1]))

	return populationLinked


#Controlling Evolution function. Actual generation iteration happens here
def Evolution(populationLinked, params):
	print("Initial Population: ")
	[ print(chromosome,end='\n') for chromosome in populationlinked.keys() ]

	#Generation loop
	for generation in range(0, params['generationNumber']):
		newPopulation = []
		fitnessList = []

		k = list(populationlinked.keys())
		for i in range(0,params["eliteSurvivors"]):
			newPopulation.append(k[i])

		#Selection->Crossover->Mutation->Population Replacement
		while len(newPopulation) != params['populationSize']:
			mates = G.tournamentSelection(populationLinked)
			offspring = G.crossover(mates)
			finalChild = G.mutation(offspring)
			newPopulation.append(finalChild)


		#Calculating Fitness, adding it to dictionary for easy lookup
		for chromosome in newPopulation:
			fitnessList.append(G.fitnessEvaluation(chromosome))
		populationLinked = dict(zip(population, fitnessList))
		populationlinked = OrderedDict(sorted(populationlinked.items(), key=lambda t: t[1]))

		display(populationLinked, generation)



def display(populationLinked, generation):
	fittest = list(populationLinked.keys())[0]
	fittestFitValue = populationLinked[fittest]
	averageFitness = int(sum(list(populationLinked.values()))/len(populationLinked))

	print("Generation Number: ", generation,end="\n")
	print("Fittest Chromosome: ", fittest ,end='\n')
	print("Travel Cost: ", fittestFitValue, end='\n')
	print("Average Fitness: ", averageFitness, end='\n')
	input("Continue...")



def main(nodes, instanceSize):

	populationLinked = generatePopulation(G.params['populationSize'], instanceSize)
	Evolution(populationLinked, G.params)


if __name__ == '__main__':
	G = GeneticOperations()
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

	main(Nodes)
