from Graph import Graph
from Genome import Genome


a0 = Genome('111', 0)
a1 = Genome('121', 1)
a2 = Genome('111', 2)
a3 = Genome('112', 3)

list_of_genomes = [a0, a1, a2, a3]


graph = Graph(list_of_genomes)
graph.MakeOptimalTree(allowed_max_distance=5)
a=6