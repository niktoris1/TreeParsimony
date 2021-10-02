from Graph import Graph
from Genome import Genome

import random

def generateGenome(length = 10, symbols = "0123", time_limits = [0, 1], genome_num = None):

    def generateString(length = 10, symbols = "0123"):
            return ''.join(random.choice(symbols) for _ in range(length))

    return Genome(generateString(length, symbols), random.uniform(time_limits[0], time_limits[1]), genome_num)


number_of_genomes = 1000
length = 10
symbols = "01"
time_limits = [0, 100]


list_of_genomes = [None for _ in range(number_of_genomes)]

for i in range(number_of_genomes):
    list_of_genomes[i] = generateGenome(length = length, symbols = symbols, time_limits = time_limits, genome_num = i)



graph = Graph(list_of_genomes)
graph.BuildHammingMatrix()
graph.BuildOptimalTree(allowed_max_distance=10)
graph.CheckIfGenealogyIsTree()
parsimony_score = graph.GetOveallParsimonyScore()
print("Parsimony score equals", parsimony_score)