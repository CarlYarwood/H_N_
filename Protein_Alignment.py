'''
Jonathan Rogers
Methods needed to convert a genetic sequence into a list of 
codons and then display said codons. 

Last Modified: 11 December 2018
'''

protein_abrv_dict = {'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
                     'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
                     'TAT':'Y','TAC':'Y','TAA':'X','TAG':'X',
                     'TGT':'C','TGC':'C','TGA':'X','TGG':'W',
                     'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
                     'CCT':'P','CCA':'P','CCG':'P','CCC':'P',
                     'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
                     'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
                     'ATT':'I','ATA':'I','ATC':'I','ATG':'M',
                     'ACT':'T','ACA':'T','ACC':'T','ACG':'T',
                     'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
                     'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
                     'GTT':'V','GTA':'V','GTC':'V','GTG':'V',
                     'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
                     'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
                     'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}

condon_length = 3

'''
demo - demonstrates all methods with a toy example
Parameter: None
return: None
'''

def demo():

    sequences = ['AAACCCTTT---GGGTTT','AAACCCTTT---CCCGGG']
    seq_names = ['Joe', 'Curly']

    protein_list = []

    for i in range(len(sequences)):
        protein_list.append(convert_bases_to_proteins(sequences[i]))


    protein_comparisons = compare_proteins(protein_list)

    display_proteins(protein_list,protein_comparisons, seq_names)

'''
protein_alignment - Takes in a list of sequences and runs the methods
to output a comparison of said sequences to the terminal

Parameters: A list of genetic sequences
            A list of the names of the genetic sequences

            The lists are assumed to be in order. Sequence name 0 is
            the name of sequence 0 and so on. 
Returns: None
'''

def protein_alignment(sequences, seq_names):

    protein_list = []

    for i in range(len(sequences)):

        protein_list.append(convert_bases_to_proteins(sequences[i]))

    protein_comparisons = compare_proteins(protein_list)

    display_proteins(protein_list,protein_comparisons, seq_names)

'''
convert_bases_to_proteins - Converts a list of genetic sequences to a
list of codons

Parameters: A list of genetic sequences

Returns: A list of codon sequences
'''


def convert_bases_to_proteins(seq):

    protein_seq = []
    codon_bases = ''
    codon = ''
    times_to_run = int(len(seq) / condon_length)

    for index in range(times_to_run):
        codon_bases = seq[0:3]

        if('-' in codon_bases):
            codon = '-'

        else:
             codon = protein_abrv_dict.get(codon_bases)

        protein_seq.append(codon)
        seq = seq[3:]

    return protein_seq

'''
compare_proteins - compares a variable list of codons and creates a 
list of the comparison results

Parameters: A list of proteins as codons

Returns: A list of codon comparisons
'''

def compare_proteins(protein_list):

    protein_comparison = []
    temp = []

    for i in range(len(protein_list[0])):
        for j in range(len(protein_list)):
            temp.append(protein_list[j][i])

        if(max(temp) == min(temp)):
            protein_comparison.append('|')
        else:
            protein_comparison.append('.')

        temp = []

    return protein_comparison

'''
display_proteins - Outputs the comparison of two protein sequences
to the terminal

Parameters: 
            1: A List of proteins
            2: A list of protein names
            3: A list of protein comparisons

Returns: None
'''

def display_proteins(protein_list, protein_comparisons, seq_names):

    bad_output = True

    list_length = len(protein_comparisons)

    while bad_output:
        
        output_length = \
        input("How many amino acids per line would you like?: ")
        print(type(output_length))

        if(not output_length.isnumeric()):
            print("Please use an integer for the protein length")

        elif(int(output_length) > list_length):
            print("Please choose a shorter number")

        else:
            output_length = int(output_length)
            bad_output = not bad_output

    full_rows = list_length//output_length
    remainder_row = list_length%output_length

    arbituary_space_num = 6

    if(len(seq_names) == 2):

        for i in range(full_rows):
            start_num = i * output_length
            end_num = i * output_length + output_length
            max_left = max(len(seq_names[0]), len(seq_names[1]))

            # Note the 6 is the number of spaces
            # in the protein sequence lines
            comparison_left =  (max_left + output_length 
            + arbituary_space_num + len(str(start_num)))

            protein_str_0 = ''.join(protein_list[0]\
            [start_num:end_num])
            protein_str_1 = ''.join(protein_list[1]\
            [start_num:end_num])
            comparison_str = ''.join(protein_comparisons)


            print(seq_names[0].ljust(max_left) + ' '*5 +
                  str(start_num) + ' ' + protein_str_0)

            print(''+str(comparison_str[start_num:end_num]).
                  rjust(comparison_left))

            print(seq_names[1].ljust(max_left) + ' '*5 +
                  str(start_num) + ' ' + protein_str_1)

            print(' ')

        if(remainder_row != 0):
            protein_str_0 = ''.join(protein_list[0]
            [end_num:list_length])
            protein_str_1 = ''.join(protein_list[1]
            [end_num:list_length])
            comparison_str = ''.join(protein_comparisons)


            print(seq_names[0].ljust(max_left) + ' '*5 +
                      str(end_num) + ' ' + protein_str_0)

            comparison_left = max_left + remainder_row\
             + arbituary_space_num + len(str(start_num))
            print(''+str(comparison_str[end_num:list_length]).
                      rjust(comparison_left))

            print(seq_names[1].ljust(max_left) + ' '*5 +
                      str(end_num) + ' ' + protein_str_1)         

    else:
        for i in range(full_rows):
            start_num = i * output_length
            end_num = i * output_length + output_length
            max_left = len(max(seq_names,key=len))
            protein_str = [''] *len(protein_list)

            # Note the 6 is the number of spaces 
            # in the protein sequence lines
            comparison_left = max_left + output_length\
             + arbituary_space_num + len(str(start_num))

            for k in range(len(protein_list)):
                protein_str[k] = ''.join(protein_list[k]
                [start_num:end_num])
                comparison_str = ''.join(protein_comparisons)

            for j in range(len(protein_list)):

                print(seq_names[j].ljust(max_left) + ' '*5 +
                      str(start_num) + ' ' + protein_str[j])
            
            comparison_left = max_left + output_length\
            + arbituary_space_num + len(str(start_num))
            print(''+str(comparison_str[start_num:end_num]).
                      rjust(comparison_left))

            print('')

if __name__ == '__main__': demo()
