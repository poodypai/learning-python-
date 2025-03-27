def main():
    dna_seq = input("Enter the DNA Sequence: ")
    
    if len(dna_seq) % 3 == 0:
        rna_seq = dna_seq.upper().replace('T', 'U')
        print("The RNA Sequence is:", rna_seq)
        
        web = 'https://alphafold.ebi.ac.uk/search/sequence/'
        protein_seq = []
        
        codontable = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
            'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
            'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
            'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
        }
        
        for x in range(0, len(rna_seq), 3):
            codon = rna_seq[x:x+3]
            amino_acid = codontable.get(codon, '?') 
            
            if amino_acid == '*':
                break
            else:
                protein_seq.append(amino_acid)
        
        protein_seq = ''.join(protein_seq)
        print("Protein Sequence is:", protein_seq)
        print("To view the 3D Structure go to:", web + protein_seq)
    else:
        print("Enter a correct DNA sequence with a length multiple of 3!")

main()
