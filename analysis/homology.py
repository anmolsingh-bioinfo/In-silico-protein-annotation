# Importing Required Packages:
from Bio.Blast import NCBIWWW          # To perform BLAST
from Bio.Blast import NCBIXML          # To read and understand output from BLAST performed
from Bio import SeqIO                  # For Biological Data + File Handling
import csv                             # For Data Handling

print("Libraries Loaded")

record = SeqIO.read("C:/Users/anmol/OneDrive/Desktop/Biopython_project/data/input_sequence.fasta", "fasta")   # Enter name of Protein FASTA file for which BLAST has to be performed

print("Sequence Fetched: Now Performing BLAST")

# Run blastp against nr database
result_handle = NCBIWWW.qblast(
    program = "blastp",
    database = "nr",
    sequence = record.seq
)

# Save BLAST output 
with open ("result.xml", "w") as b:
    b.write(result_handle.read())

print("Blast performed Successfully and results saved as result.xml")

# Parsing BLAST XML File:

with open ("result.xml") as a:
    blast_record = NCBIXML.read(a)             # Accessing BLAST output data and reading

print("Total Number of Records:" , len(blast_record.alignments))

csv_rows =[]
count = 1
for alignment in blast_record.alignments:
    print("Alignment", count, "is:")
    print(alignment.title)
    print(alignment.length)
    print(alignment.hit_id)
    
    for hsp_record in alignment.hsps:
        print(hsp_record.score)
        print(hsp_record.expect)
        print(hsp_record.query)
        print(hsp_record.sbjct)
        print(hsp_record.match)
        print(hsp_record.align_length)
        percent_identity = (hsp_record.identities/ hsp_record.align_length)*100
        print(percent_identity)
        print("Query Range:", hsp_record.query_start, "-", hsp_record.query_end)
        print("Query Range:", hsp_record.sbjct_start, "-", hsp_record.sbjct_end)
        print("-"*50)
   

        csv_rows.append([
            count,
            alignment.hit_id,
            alignment.title,
            alignment.length,
            percent_identity,
            hsp_record.score,
            hsp_record.expect,
            hsp_record.sbjct_start,
            hsp_record.sbjct_end,
            hsp_record.match
        ])

    count += 1

with open("blast.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow([
        "Alignment Number",
        "Title",
        "Length",
        "percent_identity",
        "Score",
        "E_Value",
        "Subject_Start",
        "Subject_end",
        "Match"
    ])

    writer.writerows(csv_rows)

print("Data stored successfully in csv file")

"""
So far BLAST was performed and output was interpreted and stores in csv file, which holds all neccessary information 
about the BLAST outputs:
Now, we will be analyzing this output to find:
    > Top Hit
    > What organism does it belong to?
    > E-VALUE
    
E-value Interpretation:
    E-value represents probabilty of finding a particular hit by chance
    - E < 1e-3 --> Weak
    - E < 1e-5 --> Acceptable
    - E < 1e-10 --> Strong
    - E < 1e-50 --> Almost Identical

Therefore analyzing data based on E-value scientifically means:
    " Lower the E-value, higher the confidence"
"""
# Importing Pandas for analysis:
print ("Now Analyzing Data")
import pandas as pd

print ("Pandas Imported Successfully")

df = pd.read_csv("blast.csv")

# sorting results based on E-value
df_sorted = df.sort_values(by="E_Value", ascending=True)

#Now the CSV file has been sorted based on E-value and the first row is now the best hit 

print("Data Sorted Successfully, 'Now Extracting and Analyzing Top 5 Hits")

top_hit = df_sorted.iloc[0]
top5_hits = df_sorted.head(5)

# Saving top 5 hits in new csv file
top5_hits.to_csv("top5_blast_hits.csv", index=False)

# Analysis based on e-value:
best_evalue= top_hit["E_Value"]
best_title = top_hit["Title"]

if best_evalue < 1e-50:
    confidence = "Extremely significant similarity, strong evolutionary relationship"
elif best_evalue < 1e-20:
    confidence = "Highly significant Homology detected"
elif best_evalue < 1e-5:
    confidence = "Probable Homolog, Functional Inference Possible"
else: 
    confidence = "Weak Similarity, functional annotation not reliable"


interpretation = f"""
BLAST Homology Analysis Interpretation
--------------------------------------
Best BLAST hit: {best_title}
E-value = {best_evalue}

Interpretation:
Based on the E-Value threshold analysis, this protein shows {confidence}.
The extremely low E-Value indicates that the obeserved similarity is statistically significant and unlikely to have occured by chance.

Analysis of the top-ranking BLAST hits shows that homologs sequences are present across related bacterial species, suggesting that the query protein is evolutionary converved.

Although several matching proteins are annotated as hypothetical or uncharacterized, the consistency of significant similarity across multiple organisms supports the presence of a conserved protein family. 

While BLAST analysis alone cannot assign a definitive biological functional, the strength and consistency of homology indicate that the protein is likely to play an important cellular role.
Further Functional characterization would require domain analysis or experimental validation.
"""

print(interpretation)

with open("blast_interpretation.txt", "w") as f:
    f.write(interpretation)

print("Program Exited Successfully")