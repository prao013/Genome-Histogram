import numpy as np

# Define the nucleotides
nucleotides = ['A', 'C', 'G', 'T']

# Set the length of the DNA sequence
sequence_length = 518399

# Generate random nucleotides
random_nucleotides = np.random.choice(nucleotides, sequence_length)

# Concatenate the nucleotides into a string
dna_sequence = ''.join(random_nucleotides)

print(dna_sequence)







