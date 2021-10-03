from Graph import Graph
from Genome import Genome

import random

def generateGenome(length = 10, symbols = "0123", time_limits = [0, 1], genome_num = None):

    def generateString(length, symbols):
            return ''.join(random.choice(symbols) for _ in range(length))

    return Genome(generateString(length, symbols), random.uniform(time_limits[0], time_limits[1]), None)


number_of_genomes = 100 # the running time depends qudraticaly
length = 30000 # the running time depends linearly
symbols = "ATCG"
time_limits = [0, 100]


list_of_genomes = [None for _ in range(number_of_genomes)]

for i in range(number_of_genomes):
    list_of_genomes[i] = generateGenome(length = length, symbols = symbols, time_limits = time_limits, genome_num = None)



graph = Graph(list_of_genomes)
graph.BuildHammingMatrix()
graph.BuildOptimalTree(allowed_max_distance=30000)
graph.CheckIfGenealogyIsTree()
parsimony_score = graph.GetOveallParsimonyScore()
print("Parsimony score equals", parsimony_score)