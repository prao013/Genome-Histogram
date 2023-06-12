with open('genomic.fna', 'r') as file:
    # Initialize an empty dictionary to store the 3-mers and their counts
    kmer_counts = {}
    # Iterate through the file line by line
    for line in file:
        # Skip the header line
        if line.startswith('>'):
            continue
        # Extract all the 3-mers using a sliding window approach
        for i in range(len(line) - 2):
            kmer = line[i:i+3]
            # Increment the count of the 3-mer in the dictionary
            if kmer in kmer_counts:
                kmer_counts[kmer] += 1
            else:
                kmer_counts[kmer] = 1

# Print the 3-mers and their counts
for kmer, count in kmer_counts.items():
    print(kmer)
for kmer, count in kmer_counts.items():
    print(count)


