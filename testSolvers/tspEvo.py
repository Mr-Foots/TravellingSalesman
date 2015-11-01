import random


class GeneticOperations():
	def __init__(self):

		self.params = {
			'populationSize': 20,
			'tournamentNumber': 3,
			'generationNumber': 1
		}
	def distance(self, p1, p2):
		#calculates distance from two points
		d = (((p2[0] - p1[0])**2) + ((p2[1] - p1[1])**2))**.5
		return int(d)



	def tournamentSelection(self, population):
		#randomly selects n number of candidates from the population
		selectedIndividuals = random.sample(population, self.params['tournamentNumber'])
		mates = self.fitnessEvaluation(selectedIndividuals)		#Sends the selected into fitnesseval, returns the mating candidates

		return mates


	def fitnessEvaluation(self, selectedIndividuals):
		fitnessLink = {}
		fitnessRanked = []

		#loops through the candidates to calculate their distance
		for index, candidiate in enumerate(selectedIndividuals):
			pos = 0
			travelCost = 0

			#loop will go through each node and calculate the distance between the two of them
			while pos != len(candidiate)-1:
				p1 = Nodes[str(candidiate[pos])]
				p2 = Nodes[str(candidiate[pos+1])]
				travelCost += self.distance(p2, p1) #distance formula
				pos += 1

			fitnessLink[str(travelCost)] = candidiate #create a dictionary for easy selection and matching to actual sequence

		#to find the sequences with the lowest travel time, the fitness values are sorted and matched aganist the orginal dictionary
		fitnessRanked = sorted(map(int, list(fitnessLink.keys())))
		mate = (fitnessLink[str(fitnessRanked[0])], fitnessLink[str(fitnessRanked[1])])
		
		return mate




	def crossover(self):
		pass

	def mutation(self):
		pass



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



def Evolution(population, params):


	for x in range(0, generationNumber):
		mates = []

		#run for half the population. Each mate pair will make two children
		for x in range(0, int(params['populationSize']/2)): 
			mates.append(G.tournamentSelection(population))
		while 




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
