from FASTA import getSeq
from sys import argv
from Alignment import progressive_alignment
from Align_Tool import simple_multi_sequence_output
from Align_Tool import multi_print_alignment
from pprint import pprint
from genetic_code import code

def main():
    fasta_file = getSeq(argv[1])
    #fasta_file = [["name1", "name2", "name3"], ["ATG", "ATAG", "TAG"]]
    choices = ""
    for i in range(len(fasta_file[0])):
        print(str(i) + " : " + fasta_file[0][i])
    choices = input("Enter the Associated numbers of the sequences you would like to analyze : ")
    arr_choices = [];
    temp = 0
    chunk = int(input("Enter the number of elements you would like to see on each line  : "))
    protein_input = input("Do you want protein output? [Y/n] ")
    if protein_input == 'Y' or protein_input == 'y':
        protein = True
    if protein_input == 'N' or protein_input == 'n':
        protein = False
    for i in range(len(choices)):
        if choices[i].isdigit():
            temp = (temp*10) + int(choices[i])
        elif choices[i] == " ":
            arr_choices.append(temp)
            temp = 0
    if temp != 0:
        arr_choices.append(temp)
    if len(arr_choices) < 2 :
        print("You chose one or no sequences, please choose more for an alignment")
        return
    str_to_be_align = []
    if protein:
        for i in arr_choices:
            print(i)
            rna = fasta_file[1][i].replace('T', 'U')
            aa_sequence = ''
            for i in range(0, len(rna), 3):
                codon = rna[i:i + 3]
                if codon in code:
                    aa = code[codon]
                aa_sequence += aa
            str_to_be_align.append(aa_sequence)
        align_strs = progressive_alignment(str_to_be_align, arr_choices)
    else:
        for i in arr_choices:
            print(i)
            str_to_be_align.append(fasta_file[1][i])
        align_strs = progressive_alignment(str_to_be_align, arr_choices)
    if(len(align_strs) == 3):
        for i in align_strs[0]:
            print(fasta_file[0][i])
        simple_multi_sequence_output(align_strs[1], chunk)
        #protein_strs = []

        '''
        for string in align_strs[1]:
            
            protein_strs.append(aa_sequence)
        multi_print_alignment(protein_strs, chunk)
        '''

        for i in range(len(align_strs[2])):
            print("seqs " + fasta_file[0][align_strs[0][i]] + " and " + fasta_file[0][align_strs[0][i+1]] + " is " + str(align_strs[2][i]))
    else:
        out = []
        out.append(align_strs[0])
        out.append(align_strs[1])
        simple_multi_sequence_output(out, chunk)
            
    return
main()
