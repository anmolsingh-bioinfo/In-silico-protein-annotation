## In-Silico Functional Characterization of a Conserved Bacterial Protein using Sequence Analysis and Homology-based Annotation

## Overview
This repository presents a complete bioinformatics workflow for the in-silico identification and functional characterization of a protein sequence using sequence analysis and homology-based annotation.

The project demonstrates how computational tools can be applied to analyze an initially unknown or hypothetical protein sequence, assess its quality, identify homologous proteins, and infer potential biological function using Biopython and BLAST.

---

## Introduction
The rapid advancement of genome sequencing technologies has resulted in the identification of a large number of protein-coding sequences with no experimentally validated function. Such proteins are often annotated as hypothetical or uncharacterized, highlighting a significant annotation gap in genomic databases.

Bioinformatics provides powerful computational approaches to bridge this gap by analyzing sequence features, identifying homologous proteins, and inferring biological function based on evolutionary conservation. Homology-based annotation is a foundational principle in functional genomics, as proteins with similar sequences often share similar biological roles.

This project applies a structured bioinformatics pipeline to computationally characterize a target protein sequence and infer its function using sequence quality assessment and BLAST-based homology analysis.

---

## Objective
The objectives of this project are:

- To select a biologically relevant protein sequence suitable for computational analysis  
- To perform sequence quality control and validation  
- To identify homologous protein sequences using BLASTP  
- To infer potential biological function based on homology and evolutionary conservation  
- To understand the strengths and limitations of in-silico functional annotation  

---

## Project Workflow
The analysis was performed as a single continuous pipeline:

1. Sequence Selection  
2. Sequence Quality Control  
3. Sequence Filtering and Validation  
4. Homology Search using BLASTP  
5. Functional Annotation  
6. Biological Interpretation  

Each step depends on the outcome of the previous step, mimicking real bioinformatics research workflows.

---

## Tools and Libraries Used
- Python 3  
- Biopython (SeqIO, NCBIWWW, NCBIXML)  
- Pandas  
- NCBI BLAST (BLASTP)  
- UniProt Database  

---

## Sequence Dataset
- **Input file:** `data/input_sequence.fasta`  
- **Protein:** Conserved hypothetical membrane protein  
- **UniProt ID:** Q1G9C3  
- **Organism:** *Lactobacillus delbrueckii* subsp. *bulgaricus*  
- **Sequence length:** 320 amino acids  

---

## Sequence Quality Control

### Script Used
`analysis/sequence_qc.py`

### Output File
`results/qc_summary.txt`

### Quality Parameters Assessed
- Sequence length  
- Amino acid composition  
- Presence of ambiguous residues (X)  

### QC Results
The protein sequence was 320 amino acids long, which falls within the normal size range for bacterial proteins. Amino acid composition analysis did not reveal any abnormal bias, and no ambiguous residues were detected. Based on these criteria, the sequence was considered suitable for downstream homology analysis.

---

## Homology Search using BLAST

### Script Used
`analysis/homology_analysis.py`

### BLAST Parameters
- **Program:** BLASTP  
- **Database:** NCBI non-redundant (nr)  
- **Output format:** XML  

### Generated Output Files
- `results/blast_results.xml` – Raw BLAST output  
- `results/blast_results.csv` – Parsed BLAST results  
- `results/top5_blast_hits.csv` – Top five significant BLAST hits  

### BLAST Results Summary
The BLASTP analysis identified multiple highly significant homologs across different strains of *Lactobacillus delbrueckii*. The best BLAST hit showed an E-value of **0.0**, indicating extremely strong sequence similarity and a deep evolutionary relationship.

Consistent alignment lengths and high similarity across multiple top hits suggest that the protein is evolutionarily conserved and biologically important.

---

## Functional Annotation and Biological Interpretation
Although the protein was initially annotated as hypothetical, homology analysis revealed extremely strong similarity to members of the **YidC/OxaA membrane protein insertase family**.

YidC proteins are known to play a critical role in the insertion and assembly of membrane proteins in bacterial cells. Based on the strength of homology, evolutionary conservation, and consistency across multiple BLAST hits, the target protein is inferred to function as a membrane protein insertase.

This inference is based solely on computational analysis, and experimental validation would be required to confirm the exact biological role.

A detailed interpretation of the BLAST results is available in:
`results/blast_interpretation.txt`

---

## Conclusion
This project demonstrates the application of a structured bioinformatics pipeline for the in-silico functional characterization of a protein sequence. Sequence quality control confirmed the suitability of the protein for analysis, and BLAST-based homology search revealed extremely significant similarity to the YidC family of membrane protein insertases.

The study highlights the importance of homology-based annotation in functional genomics and emphasizes the need for cautious interpretation when relying solely on computational predictions.

---
## Author
**Anmol Singh**  
B.Sc. Biotechnology  
School of Life Sciences and Biotechnology  
Chhatrapati Shahu Ji Maharaj University, Kanpur

