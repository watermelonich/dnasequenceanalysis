# Consider the DNA sequence, AGTTAGCTAGGAG

# We'll make our model process the following questions:
# How many nucleotides are present?
# Calculate the percentage GC in the sequence.
# How many purines are present?
# How many pyrimidines are present?
# Calculate the percentage of purines in the sequence.

dna = "AGTTAGCTAGGAG"

print("\n")
# How many nucleotides are present?
number_of_nucleotides = len(dna)
print("Number of nucleotides: ", number_of_nucleotides)
print("\n")

# Calculate the percentage GC in the sequence.
gc = dna.count('G') + dna.count('C')
length_of_dna = len(dna)
gc_percentage = gc / length_of_dna * 100
print("Percentage of GC: ", gc_percentage)
print("\n")

gc_rounded=round(gc_percentage, 2)
print("Percentage of GC")
print("\n")

# How many purines are present?
purines = dna.count('A') + dna.count('G')
print("Number of purines: ", purines)
print("\n")

# How many pyrimidines are present?
pyramidines = dna.count('C') + dna.count('T')
print("Number of pyramidines: ", pyramidines)
print("\n")

# Calculate the percentage of purines in the sequence.
percentage_purines = purines / length_of_dna * 100
print("Percentage of purines: ", percentage_purines)
print("Percentage rounded: ", round(percentage_purines, 2))
print("\n")

