import random
import os
from collections import OrderedDict

class GeneticOperations():
	def __init__(self):
		self.params = {
			'populationSize': 200,
			'tournamentNumber': 4,
			'elitismRate': float(1/10),
			'generationNumber': 200,
			'mutationRate': (1,2,3,4)
		}
		self.params['eliteNum']= int(self.params['populationSize'] * self.params['elitismRate'])

	def distance(self, p1, p2):
		#calculates distance from two points
		return int((((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**.5)

	def tournamentSelection(self, populationLinked):
		"""
			Function will select three chromosomes, then make the mating pair
			fitnessOrdered sorts the chromosomes by fitness and returns the first two(lowest fitness)
		"""

		#randomly selects n number of chromosomes from the population. Sample is great because it cannot select repeats
		selectedChromosomes = random.sample(list(populationLinked.items()), self.params['tournamentNumber'])
		fitnessOrdered = sorted(selectedChromosomes, key=lambda t: t[1])
		return (fitnessOrdered[0][0], fitnessOrdered[1][0]) #Returns the mates




	def fitnessEvaluation(self, chromosome):
		"""
			Takes an chromosome, returns the fitness value (travelCost) by summing the costs of each node
			A more fit chromosome will have a lower fitness value (held by var travelCost)
		"""

		travelCost = sum((self.distance(Nodes[chromosome[i-1]], Nodes[chromosome[i]]) for i in range(1, len(chromosome))))
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

		return offspring

	def mutation(self, chromosome):
		"""
			Mutation is vital to add genetic diversity
			a random number, r, is generated and if that matches the mutation rate then a swap mutation will occur
			a swap is necessary in order to produce a valid sequence
		"""
		r = random.randint(1,100)
		if r in self.params['mutationRate']:
			points = sorted(random.sample(list(range(1,len(chromosome))), 2))
			chromosome[points[0]], chromosome[points[1]] = chromosome[points[1]], chromosome[points[0]]
			return tuple(chromosome)
		else:
			return tuple(chromosome)

#Function will create initial Population. Size is length of pop, eleSize is length of TSP
def generatePopulation(pSize, instanceSize):
	"""
	Creates the initial population. 1 is the origin so it must be the first node
	"""

	P = [] #holds population
	F = []  #holds Fitness values
	lang = tuple(range(2,instanceSize+1)) #generating the 'alphabet' for nodes

	#Loop creates the n number of chromosomes
	for individualChromosome in range(0, pSize):

		chromosome = []
		possible = list(lang)

		#loops to create visiting sequence
		while len(possible) != 0:
			selected = random.choice(possible) #randomly chooses a possible node
			del possible[possible.index(selected)] #deletes that node so it doesnt repeat
			chromosome.append(selected)

		chromosome.insert(0,1)
		f = G.fitnessEvaluation(chromosome)



		F.append(f)
		P.append(tuple(chromosome))

	populationLinked = dict(zip(P,F))
	populationLinked = OrderedDict(sorted(populationLinked.items(), key=lambda t: t[1]))


	return populationLinked


#Controlling Evolution function. Actual generation iteration happens here
def Evolution(populationLinked, params):

	bestChromosome = list(populationLinked.items())[0]
	stagnationCounter = 0
	#Generation loop
	for generation in range(0, params['generationNumber']):

		newPopulation = []
		fitnessList = []

		#Elitism
		elite = list(populationLinked.keys())[:params['eliteNum']]
		fittestElite = list(populationLinked.items())[0]

		if fittestElite[1] == bestChromosome[1]:
			stagnationCounter += 1
		elif fittestElite[1] < bestChromosome[1]:
			stagnationCounter = 0
			bestChromosome = fittestElite
			del elite[elite.index(fittestElite[0])]

		if stagnationCounter == 20:
			print("Solution Stagnation Detected. Stopping...\n\n")
			break

		newPopulation.append(bestChromosome[0])
		newPopulation.extend(elite)



		#Selection->Crossover->Mutation->Population Replacement
		while len(newPopulation) != params['populationSize']:
			mates = G.tournamentSelection(populationLinked)
			offspring = G.crossover(mates)
			finalOffspring = G.mutation(offspring)
			newPopulation.append(finalOffspring)


		#Calculating Fitness, adding it to dictionary for easy lookup
		fitnessList = [G.fitnessEvaluation(chromosome) for chromosome in newPopulation]
		populationLinked = dict(zip(newPopulation, fitnessList))
		populationLinked = OrderedDict(sorted(populationLinked.items(), key=lambda t: t[1]))

		display(populationLinked, generation, bestChromosome)

	print('\n\n\n######################')
	print('Final Best Chromosome: ', bestChromosome[0])
	print('Best Travel Cost: ', bestChromosome[1])

def display(populationLinked, generation, bestChromosome):
	if len(populationLinked) > 150:
		print('Generation: ', generation)
		return
	fittest = list(populationLinked.keys())[0]
	fittestFitValue = populationLinked[fittest]
	averageFitness = int(sum(list(populationLinked.values()))/len(populationLinked))

	print("\n")
	print("------------------")
	print("Generation Number: ", generation,end="\n")
	print('Best Chromosome: ', bestChromosome[0],end='\n')
	print('Travel Cost: ', bestChromosome[1],end='\n')
	print("Fittest Chromosome: ", fittest ,end='\n')
	print("Travel Cost: ", fittestFitValue, end='\n')
	print("Average Fitness: ", averageFitness, end='\n')



def main(nodes=None, instanceSize=None):
	global G
	global Nodes

	os.system('cls')
	Nodes = nodes
	G = GeneticOperations()
	populationLinked = generatePopulation(G.params['populationSize'], instanceSize)
	Evolution(populationLinked, G.params)
