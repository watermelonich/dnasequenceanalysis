def count_nucleotides(sequence):
    return len(sequence)

def calculate_gc_percentage(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    length = len(sequence)
    return gc_count / length * 100

def count_purines(sequence):
    return sequence.count('A') + sequence.count('G')

def count_pyrimidines(sequence):
    return sequence.count('C') + sequence.count('T')

def calculate_purine_percentage(sequence):
    purine_count = count_purines(sequence)
    length = len(sequence)
    return purine_count / length * 100

def analyze_dna_sequence(sequence):
    results = {}
    results["Number of nucleotides"] = count_nucleotides(sequence)
    results["Percentage of GC"] = calculate_gc_percentage(sequence)
    results["Number of purines"] = count_purines(sequence)
    results["Number of pyrimidines"] = count_pyrimidines(sequence)
    results["Percentage of purines"] = calculate_purine_percentage(sequence)
    return results

def read_dna_sequence_from_file(file_path):
    with open(file_path, 'r') as file:
        sequence = file.readline().strip()
    return sequence

def main():
    dna_sequence = read_dna_sequence_from_file('dnadata_input.txt')
    results = analyze_dna_sequence(dna_sequence)
    for key, value in results.items():
        print(f"{key}: {value:.2f}")

    with open('dnaanalysis_output.txt', 'a') as output_file:
        output_file.write(f"DNA Sequence: {dna_sequence}\n\n")
        for key, value in results.items():
            output_file.write(f"{key}: {value:.2f}\n")
        output_file.write("\n")

    with open('output.txt', 'w') as output_file:
        output_file.write(f"DNA Sequence: {dna_sequence}\n\n")
        for key, value in results.items():
            output_file.write(f"{key}: {value:.2f}\n")
        output_file.write("\n")
    
    print("Analysis results and DNA sequence saved to output.txt")
    print("Analysis results appended to dnaanalysis_output.txt")

if __name__ == "__main__":
    main()
