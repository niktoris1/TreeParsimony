import sys

import numpy
import numpy as np


class Genome:
    def __init__(self, genome_string, sample_time, genome_num):
        self.genome_string = genome_string
        self.sample_time = sample_time
        self.chosen_parent = None
        self.distance_to_parent = sys.maxsize
        self.genome_num = genome_num

        self.genome_string_as_nparray = None
        self.genome_string_as_numpy_binary_array = self.genomeStringToNumpyBinaryArray()


    def printGenome(self):
        print('Genome string:', self.genome_string, 'Sampled at time', self.sample_time)

    def genomeStringToNumpyBinaryArray(self):

        nparray = numpy.zeros(4*len(self.genome_string))

        def letterToBinary(letter):
            if letter == "A":
                return [1, 0, 0, 0]
            elif letter == "C":
                return [0, 1, 0, 0]
            elif letter == "G":
                return [0, 0, 1, 0]
            elif letter == "T":
                return [0, 0, 1, 0]
            else:
                print("Unrecognized letter")
                raise ValueError


        for char_num in range(len(self.genome_string)):
            nparray[4*char_num : 4*char_num+4] = letterToBinary(self.genome_string[char_num])

        return nparray


def hammingDistance(first_genome, second_genome):

    if len(first_genome.genome_string) != len(second_genome.genome_string):
        print('Genome string lengths are not equal')
        raise ValueError

    twodistance = np.count_nonzero(first_genome.genome_string_as_numpy_binary_array != second_genome.genome_string_as_numpy_binary_array)

    #for cite_num in range(len(first_genome.genome_string)):
    #    if first_genome.genome_string[cite_num] != second_genome.genome_string[cite_num]:
    #        distance += 1

    return twodistance/2