"""
Module 01 for In-Silico Analysis of an unknown/hypothetical protein sequence.
Objective of this module to perform qquality analysis to check whether the selected sequence is suitable for further downstream processing or not.

This Module is built using Biopython module and basic python iterations..
"""
from Bio import SeqIO    #importing the required module

record = SeqIO.read(
    "C:/Users/anmol/OneDrive/Desktop/Biopython_project/data/input_sequence.fasta",
    "fasta")             # parsing the protein sequence/FASTA File

# to prevent any path errors, directly paste the input_sequence file path 

print ("Sequence fetched successfully")

sequence = str(record.seq) # converts the biological sequence from Seqrecord into normal python string which allows wast iteration and counting

protein_length = len(sequence)  #calculates the number of amino acids in the protein 

# Amino Acid Frequency calculation
aa_counts = {}    #empty dictionary that store amino acid counts

for aa in sequence:
    aa_counts[aa] = aa_counts.get(aa, 0)+ 1      #Loops through each a.a. in sequence, get it and count how many times each amino acid is present 

aa_percent = {}  #dictionary - stores amino acid percentage

for aa, count in aa_counts.items():
    aa_percent[aa] = (count/protein_length)*100       #check count of each type of amino acid in aa_counts to calculate  percentage composition of each

ambiguous_count = aa_counts.get("X", 0)     #counts for unknown amino acids present in the sequence

print("Quality Analysis Done....")

#writes qc result in a file
with open("C:/Users/anmol/OneDrive/Desktop/Biopython_project/result/qc_summary.txt", "w") as result:
    result.write("SEQUENCE QUALITY CONTROL REPORT\n")
    result.write(f"Protein ID: {record.id}\n")
    result.write(f"Sequence length: {protein_length} amino acids\n\n")
    result.write("Amino acid composition(%):\n")

    for aa in sorted(aa_percent.keys()):
        result.write(f"{aa}: {aa_percent[aa]:.2f}\n")    #write amino acid composition in alphabetical order 

    result.write(f"\nNumber of ambiguous residues (X): {ambiguous_count}\n\n")

    if protein_length>=100 and ambiguous_count==0:
        result.write("QC Decision: Sequence is suitable for dowstream analysis.\n")
    else:
        result.write("QC Decision: Sequence may not be suitable for downstream analysis.\n")


print("Program Exited Successfully; QC Performed - Results Saved as qc_summary.txt")