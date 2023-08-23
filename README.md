# DNA Sequence Analysis

Analyze DNA sequences and calculate various properties.

## Introduction

This simple DNA sequence analysis script allows you to analyze DNA sequences and calculate fundamental properties such as nucleotide counts, GC percentage, purine and pyrimidine counts, and more.

## Usage

1. Place the DNA sequence you want to analyze in a file named `dnadata_input.txt`. The sequence should be on the first line of the file.

2. Run the script:

   ```
   python dnaseqanalysis.py
   ```
   
View the analysis results in the terminal. The script will print out properties like nucleotide counts, GC percentage, and more.
The results are also saved in the output.txt file.

** Files
1. dna_sequence_analysis.py: The main script for analyzing DNA sequences.
2. dnadata_input.txt: Input file containing the DNA sequence to be analyzed.
3. output.txt: Output file containing the analysis results.

** Example:
If you have a DNA sequence "AGCTAGCTAG", place it in dnadata_input.txt and run the script. You'll see results similar to:

  ```
  Number of nucleotides: 10.00
  Percentage of GC: 50.00
  Number of purines: 6.00
  Number of pyrimidines: 4.00
  Percentage of purines: 60.00
  ```

** Note: This project is a simplified version for demonstration purposes and doesn't require any external dependencies or virtual environments.

## Contributing

Contributions to this project are welcome! Feel free to open issues, submit pull requests, or provide feedback. However, as this project is not yet optimized or complete, please keep that in mind when contributing.

## License

This project is licensed under the [MIT License](LICENSE).
