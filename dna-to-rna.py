def menu():
    dna_seq=[]
    dna_seq = input("Enter the DNA Sequence ")
    rna_seq = dna_seq.upper().replace('T','U')
    print("The RNA Sequence is: ", rna_seq)

menu()
