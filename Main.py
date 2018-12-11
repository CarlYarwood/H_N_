'''
Main - handles initial user input, calls necessary functions, and 
gives alignment output. 

10 Dec 2018 
'''




from FASTA import getSeq
from sys import argv
from Alignment import progressive_alignment
from Align_Tool import simple_multi_sequence_output
from Align_Tool import multi_print_alignment
from pprint import pprint
from genetic_code import code
'''
Main method
ran when program is called
takes a command line argument for a fasta file
displays sequences in fasta file and asks which you would like to align
then asks for the number of chars to display on each line
then finally alsk weather you would like an ouput in protein or neucleotide
then generates ouput
'''
def main():
    #reads in fasta files
    fasta_file = getSeq(argv[1])
    choices = ""
    #Displays different choices with associated numbers
    for i in range(len(fasta_file[0])):
        print(str(i) + " : " + fasta_file[0][i])
        #reads in choices
    choices = input("Enter the Associated numbers of the sequences you would like to analyze : ")
    arr_choices = [];
    temp = 0
    #reads in value of how many elements to display on each line
    chunk = int(input("Enter the number of elements you"+
                      ("would like to see on each line  : ")))
    #determines wheather alignmen is to be done with protiens or nuecleotides
    protein_input = input("Do you want protein output? [Y/n] ")
    if protein_input == 'Y' or protein_input == 'y':
        protein = True
    if protein_input == 'N' or protein_input == 'n':
        protein = False
    #gets choices from string and parses them into digits
    for i in range(len(choices)):
        if choices[i].isdigit():
            temp = (temp*10) + int(choices[i])
        elif choices[i] == " ":
            arr_choices.append(temp)
            temp = 0
    if temp != 0:
        arr_choices.append(temp)
    #checks to see if enough sequences where entered to actually do an alignment
    if len(arr_choices) < 2 :
        print("You chose one or no sequences, "
              +("please choose more for an alignment"))
        return
    
    str_to_be_align = []
    #does protien output if protien
    if protein:
        for i in arr_choices:
            print(i)
            #changes nucleotides to rna
            rna = fasta_file[1][i].replace('T', 'U')
            aa_sequence = ''
            #constructs amino acid sequence
            for i in range(0, len(rna), 3):
                codon = rna[i:i + 3]
                if codon in code:
                    aa = code[codon]
                aa_sequence += aa
            str_to_be_align.append(aa_sequence)
        #aligns sequences
        align_strs = progressive_alignment\
                     (str_to_be_align, arr_choices)
        #in nucleotide case
    else:
        #generates array to be passed to method
        for i in arr_choices:
            print(i)
            str_to_be_align.append(fasta_file[1][i])
        #passes array to method to aling strings
        align_strs = progressive_alignment\
                     (str_to_be_align, arr_choices)
    #determines wheather we are doing two string output or more than two
    #string output
    if(len(align_strs) == 3):
        #more then two string output
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
            print("seqs "
                  + (fasta_file[0][align_strs[0][i]])
                  + ( " and ")
                  + (fasta_file[0][align_strs[0][i+1]])
                  + (" is ")
                  + (str(align_strs[2][i])))
    else:
        #two string output
        out = []
        out.append(align_strs[0])
        out.append(align_strs[1])
        simple_multi_sequence_output(out, chunk)
            
    return
main()
