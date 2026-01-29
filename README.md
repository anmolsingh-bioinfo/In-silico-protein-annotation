## In-Silico Identification and Functional Characterization of a Target Protein Sequence using Sequence Analysis and Homology-based Annotation

This repository contains a bioinformatics pipeline for the in-silico analysis and functional annotation of a protein sequence using sequence quality assessment and homology-based approaches.

The project demonstrates how unknown or initially hypothetical protein sequences can be computationally analyzed to infer biological function using Biopython and NCBI BLAST.

---
## Project Objective
- To assess the quality of a protein sequence
- To identify homologous proteins using BLASTP
- To infer potential biological function based on evolutionary conservation
- To understand the strengths and limitations of homology-based functional annotation

---
## Pipeline Workflow
1. Sequence selection from UniProt
2. Sequence quality control (length, amino acid composition, ambiguous residues)
3. Homology search using BLASTP against the NCBI nr database
4. Parsing and filtering of BLAST results
5. Functional inference and biological interpretation

---

## Tools and Libraries Used
- Python 3
- Biopython
- NCBI BLAST (BLASTP)
- Pandas (for result parsing and sorting)

---

## Key Findings
- The selected protein sequence passed quality control checks.
- BLASTP analysis revealed extremely significant similarity to the YidC/OxaA membrane protein insertase family.
- Strong evolutionary conservation suggests an essential cellular role.
- Functional inference was made cautiously based on homology, without experimental claims.

---
## Directory Strucutre
- data/ - Input FASTA sequence
- analysis/ - Python scripts for QC and BLAST analysis
- results/- Output files generated at each step
