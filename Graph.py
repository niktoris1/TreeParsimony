import sys

from Genome import Genome, hammingDistance

class Graph:
    def __init__(self, genome_list):
        self.genome_list = genome_list

    def MakeOptimalTree(self, allowed_max_distance=sys.maxsize):

        def TakeTime(genome):
            return genome.sample_time

        for genome in self.genome_list:
            for another_genome in self.genome_list:
                if genome is another_genome:
                    continue
                else:
                    if hammingDistance(genome, another_genome) <= allowed_max_distance:
                        if (genome.sample_time < another_genome.sample_time) or \
                                (genome.sample_time == another_genome.sample_time and
                                 genome.genome_string < another_genome.genome_string):
                            another_genome.suitable_parents.append(genome)
                            genome.suitable_children.append(another_genome)


        for genome in self.genome_list:
            if genome.suitable_parents == []:
                genome.suitable_parents = None
            else:
                genome.chosen_parent = min(genome.suitable_parents, key=TakeTime)

        for genome in self.genome_list:
            if genome.chosen_parent != None:
                genome.chosen_parent.chosen_child = genome






