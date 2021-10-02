import sys
import time

from Genome import Genome, hammingDistance

class Graph:
    def __init__(self, genome_list):
        self.genome_list = genome_list
        genome_list.sort(key=self.TakeTime) # genomes are sorted by time automatically
        self.hamming_matrix = None
        self.tree_built = False

        for genome_num in range(len(self.genome_list)):
            self.genome_list[genome_num].genome_num = genome_num

    def TakeTime(self, genome):
        return genome.sample_time

    def BuildHammingMatrix(self):

        time1 = time.time()
        matrix_size = len(self.genome_list)

        self.hamming_matrix = [[0 for i in range(matrix_size)] for j in range(matrix_size)]

        for first_genome_num in range(matrix_size):
            for second_genome_num in range(first_genome_num+1, matrix_size):
                #Hamming on the diagonal is zero and the matrix is symmetrical
                self.hamming_matrix[first_genome_num][second_genome_num] = \
                    hammingDistance(self.genome_list[first_genome_num], self.genome_list[second_genome_num])
                self.hamming_matrix[second_genome_num][first_genome_num] = self.hamming_matrix[first_genome_num][second_genome_num]

        time2 = time.time()
        print("Hamming matrix built in", time2 - time1, "seconds")

    def GetPrecomputedHammingDistance(self, first_genome_num, second_genome_num):
        if self.hamming_matrix == None:
            print("Hamming matrix not yet computed")
            raise ValueError
        return self.hamming_matrix[first_genome_num][second_genome_num]

    def BuildOptimalTree(self, allowed_max_distance=sys.maxsize):

        time_start = time.time()

        # maybe the number of choices might be shrinked a bit

        for first_genome_num in range(len(self.genome_list)):
            first_genome = self.genome_list[first_genome_num]
            for second_genome_num in range(first_genome_num+1, len(self.genome_list)):
                second_genome = self.genome_list[second_genome_num]
                if self.GetPrecomputedHammingDistance(first_genome_num, second_genome_num) <= allowed_max_distance:
                    if self.GetPrecomputedHammingDistance(first_genome_num, second_genome_num) < \
                        self.genome_list[second_genome_num].distance_to_parent:
                        second_genome.chosen_parent = first_genome
                        second_genome.distance_to_parent = self.GetPrecomputedHammingDistance(first_genome_num, second_genome_num)

        self.tree_built = True

        time_finish = time.time()

        print("Tree built in", time_finish-time_start, "seconds")

    def GetOveallParsimonyScore(self):
        if self.tree_built == False:
            print("No tree is built yet. Cannot compute a parsimony score")
            raise ValueError
        else:
            overall_parsimony_score = 0
            for genome_num in range(len(self.genome_list)):
                if self.genome_list[genome_num].chosen_parent != None:
                    overall_parsimony_score += self.GetPrecomputedHammingDistance(genome_num,
                        self.genome_list[genome_num].chosen_parent.genome_num)

        return overall_parsimony_score

    def CheckIfGenealogyIsTree(self):
        if self.tree_built == False:
            print("Build the tree first")
            raise ValueError
        for genome in self.genome_list:
            if genome.chosen_parent == None and genome.genome_num != 0:
                print("Some genome, which is not the first one is the root. "
                      "That means, that we have several subtrees in the genealogy. The package cannot process it yet, exiting.")
                raise ValueError
            if genome.chosen_parent != None and genome.sample_time < genome.chosen_parent.sample_time:
                print("Genome has its parent sampled later, than him. It is impossible")
                raise ValueError
            if genome.chosen_parent != None and (genome.sample_time == genome.chosen_parent.sample_time) and (genome.genome_num >= genome.chosen_parent.genome_num):
                print("There seems to be a problem with incostintency of tackling the genones with the same time. Proceed with caution")
        print("The genealogy seems to be a tree-like structure with correct edges")


