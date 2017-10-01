###########################################################
'''
GENETIC ALGORITHM IN PYTHON FROM SCRATCH (made by S K Aravind)

Steps:
1. Create Population (new DNA created)
2. Evaluate Fitnesses
3. Natural Selection (Choose which species can transfer DNA to next generation), probabilistically.
4. Cross over (Mating/ Reproduction)
5. Tiny mutation in DNA
6. Repeat until you get THE PERFECT species :P

Problem I'm solving is inspired by Daniel Shiffman's awesome video on genetic algorithm. The problem is
to create a particular string, from randomly generated species of strings using genetic algo.
He demonstrated it using JavaScript and the target phrase was "To be or not to be is the question"
'''
###########################################################


# Some Global Variables
population = 1000
target = raw_input("Enter Target DNA: ")
recordFitness = 0
species = []
nextGen = []
selected = []
fitnesses = []
mutationRate = 0.003  # 0.5 percent mutation
generation = 1

import string, random , os, time #Duh



maxFitness = len(target)


# FUNCTIONS
###########################################################

# Evaluates fitness, Fitness = no of characters common between target DNA and species DNA
def evaluateFitness(species):
	for s in species:
		fitness = 0
		for i in range(len(target)):
			if target[i] == s.DNA[i]:
				fitness+=1
		s.fitness = fitness
		fitnesses.append(fitness)


# Sorts the species based on fitness values
def Rank(species):
	species.sort(key=lambda x:x.fitness, reverse = True)


# Adds random mutation based on the mutation rate global variable
def Mutation(spec, MR):
	for sp in range(len(spec)):
		specresult = ''
		speclist = []
		for w in spec[sp]:
			speclist.append(w)
		for i in range(len(speclist)):
			prob = random.random()
			if prob<=MR:
				speclist[i] = random.choice(string.letters+' '+','+'.')
			else:
				pass
		for w in speclist:
			specresult += w
		spec[sp] = specresult

	return spec


# uses Accept/ Reject algorithm for pool selection
def getMate(species):
	while(True):
		choice = int(random.random()*population)
		prob = species[choice].fitness**4
		selection = (random.random()*maxFitness)**4
		if selection < prob:
			return species[choice]


# Mix the DNA of the two mates
def CrossOver(species):
	tot = len(species)
	newgen = []
	childrenObjs = []
	for i in range(population):
		children = ''
		mate1 = getMate(species)
		mate2 = getMate(species)
		p = int(random.random()*len(target))
		for i in range(p):
			children = children + mate1.DNA[i]
		for j in range(p,len(target)):
			children = children + mate2.DNA[j]
		newgen.append(children)
	
	newgen = Mutation(newgen, mutationRate)

	for i in range(population):
		newspecies = Species()
		newspecies.DNA = newgen[i]
		childrenObjs.append(newspecies)

	return childrenObjs


# prints average fitness of the generation
def printAverageFitness(species, gen):
	total = 0
	for s in species:
		total += s.fitness
	avg = float(total)/(len(species))
	print('\nGeneration %d average fitness = %.3f'%(gen,avg))


# function for random DNA creation (1st step)
def RandomSpecies():
		s = ''
		for i in range(len(target)):
			s = s + random.choice(string.letters+' '+','+'.')
		return s


# creates species objects with random DNA value
def GiveBirth(pop, species, nextGen):
	if len(nextGen)==0 or len(species)==0:
		for i in range(pop):
			sps = Species()
			species.append(sps)

###########################################################


# SPECIES CLASS

class Species:
	def __init__(self):
		self.DNA = RandomSpecies()

			

### LET THE EVOLUTION BEGIN :D ###


while(1):
	os.system('cls')
	if target.isalpha():

		print('GENERATION: %d\t Target: \'%s\'\n\tPopulation:%d\n\n\tTop 5'%(generation,target,population))
		GiveBirth(population, species, nextGen)
		evaluateFitness(species)
		#selected = NaturalSelection(species)
		Rank(species)
		for i in range(5):
			print('DNA : %s   Fitness: %d' %(species[i].DNA, species[i].fitness))
		print('\n\tWorst 5')
		for i in range(5):
			print('DNA : %s   Fitness: %d' %(species[population - i - 1].DNA, species[population - i - 1].fitness))
		recordFitness = species[0].fitness
		printAverageFitness(species, generation)
		if species[0].DNA == target:
			print('\n\nFinally \'%s\' was born. Happy Bday, species :D\n\n\n\n' %species[0].DNA )
			break
		nextGen = CrossOver(species)
		species = nextGen # kill all previous gen and start the evolution again with new gen
		generation += 1
	else:
		print("Error: Entered Target Should be String")
		break


	
	#time.sleep(0.05)

	#break #for debugging purposes
