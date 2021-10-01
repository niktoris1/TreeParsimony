class Genome:
    def __init__(self, genome_string, sample_time):
        self.genome_string = genome_string
        self.sample_time = sample_time
        self.suitable_parents = []
        self.suitable_children = []
        self.chosen_parent = None
        self.chosen_child = None

    def printGenome(self):
        print('Genome string:', self.genome_string, 'Sampled at time', self.sample_time)



def hammingDistance(first_genome, second_genome):

    if len(first_genome.genome_string) != len(second_genome.genome_string):
        print('Genome string lengths are not equal')
        raise ValueError

    distance = 0

    for cite_num in range(len(first_genome.genome_string)):
        if first_genome.genome_string[cite_num] != second_genome.genome_string[cite_num]:
            distance += 1

    return distance