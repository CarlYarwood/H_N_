protein_dict = {'TTT':'Phe','TTC':'Phe','TTA':'Leu','TTG':'Leu','TCT':'Ser',
                'TCC':'Ser','TCA':'Ser','TCG':'Ser','TAT':'Tyr','TAC':'Tyr',
                'TAA':'Ter','TAG':'Ter','TGT':'Cys','TGC':'Cys','TGA':'Ter',
                'TGG':'Trp','CTT':'Leu','CTC':'Leu','CTA':'Leu','CTG':'Leu',
                'CCT':'Pro','CCA':'Pro','CCG':'Pro','CCC':'Pro','CAT':'His',
                'CAC':'His','CAA':'Gln','CAG':'Gln','CGT':'Arg','CGC':'Arg',
                'CGA':'Arg','CGG':'Arg','ATT':'Ile','ATA':'Ile','ATC':'Ile',
                'ATG':'Met','ACT':'Thr','ACA':'Thr','ACC':'Thr','ACG':'Thr',
                'AAT':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys','AGT':'Ser',
                'AGC':'Ser','AGA':'Arg','AGG':'Arg','GTT':'Val','GTA':'Val',
                'GTC':'Val','GTG':'Val','GCT':'Ala','GCC':'Ala','GCA':'Ala',
                'GCG':'Ala','GAT':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
                'GGT':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}

protein_abrv_dict = {'TTT':'F','TTC':'F','TTA':'L','TTG':'L','TCT':'S',
                     'TCC':'S','TCA':'S','TCG':'S','TAT':'Y','TAC':'Y',
                     'TAA':'X','TAG':'X','TGT':'C','TGC':'C','TGA':'X',
                     'TGG':'W','CTT':'L','CTC':'L','CTA':'L','CTG':'L',
                     'CCT':'P','CCA':'P','CCG':'P','CCC':'P','CAT':'H',
                     'CAC':'H','CAA':'Q','CAG':'Q','CGT':'R','CGC':'R',
                     'CGA':'R','CGG':'R','ATT':'I','ATA':'I','ATC':'I',
                     'ATG':'M','ACT':'T','ACA':'T','ACC':'T','ACG':'T',
                     'AAT':'N','AAC':'N','AAA':'K','AAG':'K','AGT':'S',
                     'AGC':'S','AGA':'R','AGG':'R','GTT':'V','GTA':'V',
                     'GTC':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A',
                     'GCG':'A','GAT':'D','GAC':'D','GAA':'E','GAG':'E',
                     'GGT':'G','GGC':'G','GGA':'G','GGG':'G'}


Brisbane_H1_N1 = 'ATGAAAGTAAAACTACTGGTCCTGTTATGCACATTTACAGCTACATATGCAGACACAATATGTATAGGCT\
ACCATGCTAACAACTCGACCGACACTGTTGACACAGTACTTGAAAAGAATGTGACAGTGACACACTCTGT\
CAACCTGCTTGAGAACAGTCACAATGGAAAACTATGTCTATTAAAAGGAATAGCCCCACTACAATTGGGT\
AATTGCAGCGTTGCCGGGTGGATCTTAGGAAACCCAGAATGCGAATTACTGATTTCCAAGGAGTCATGGT\
CCTACATTGTAGAAAAACCAAATCCTGAGAATGGAACATGTTACCCAGGGCATTTCGCTGACTATGAGGA\
ACTGAGGGAGCAATTGAGTTCAGTATCTTCATTTGAGAGGTTCGAAATATTCCCCAAAGAAAGCTCATGG\
CCCAACCACACCGTAACCGGAGTGTCAGCATCATGCTCCCATAATGGGGAAAGCAGTTTTTACAGAAATT\
TGCTATGGCTGACGGGGAAGAATGGTTTGTACCCAAACCTGAGCAAGTCCTATGCAAACAACAAAGAAAA\
AGAAGTCCTTGTACTATGGGGTGTTCATCACCCGCCAAACATAGGTAACCAAAAGGCCCTCTATCATACA\
GAAAATGCTTATGTCTCTGTAGTGTCTTCACATTATAGCAGAAAATTCACCCCAGAAATAGCCAAAAGAC\
CCAAAGTAAGAGATCAAGAAGGAAGAATCAATTACTACTGGACTCTGCTTGAACCCGGGGATACAATAAT\
ATTTGAGGCAAATGGAAATCTAATAGCGCCAAGATATGCTTTCGCACTGAGTAGAGGCTTTGGATCAGGA\
ATCATCAACTCAAATGCACCAATGGATAAATGTGATGCGAAGTGCCAAACACCTCAGGGAGCTATAAACA\
GCAGTCTTCCTTTCCAGAACGTACACCCAGTCACAATAGGAGAGTGTCCAAAGTATGTCAGGAGTGCAAA\
ATTAAGGATGGTTACAGGACTAAGGAACATCCCATCCATTCAATCCAGAGGTTTGTTTGGAGCCATTGCC\
GGTTTCATTGAAGGGGGGTGGACTGGAATGGTAGATGGTTGGTATGGTTATCATCATCAGAATGAGCAAG\
GATCTGGCTATGCTGCAGATCAAAAAAGCACACAAAATGCCATTAATGGGATTACAAACAAGGTGAATTC\
TGTAATTGAGAAAATGAACACTCAATTCACAGCAGTGGGCAAAGAATTCAACAAATTGGAAAGAAGGATG\
GAAAACTTGAATAAAAAAGTTGATGATGGGTTTATAGACATTTGGACATATAATGCAGAACTGTTGGTTC\
TACTGGAAAATGAAAGGACTTTGGATTTCCATGACTCCAATGTGAAGAATCTGTATGAGAAAGTAAAAAG\
CCAGTTAAAGAATAATGCTAAAGAAATAGGAAATGGGTGTTTTGAATTCTATCACAAGTGTAACGATGAA\
TGCATGGAGAGTGTAAAGAATGGAACTTATGACTATCCAAAATATTCCGAAGAATCAAAGTTAAACAGGG\
AGAAAATTGATGGAGTGAAATTGGAATCAATGGGAGTCTATCAGATTCTGGCGATCTACTCAACAGTCGC\
CAGTTCTCTGGTTCTTTTGGTCTCCCTGGGGGCAATCAGCTTCTGGATGTGTTCCAATGGGTCTTTACAG\
TGTAGAATATGCATCTAAGACCAGAATTTCAGAAATATAAGGAAAAACACCCTTGTTTCTACT'

Cali_H1_N1 = 'ATGAAGGCAATACTAGTAGTTCTGCTATATACATTTGCAACCGCAAATGCAGACACATTATGTATAGGTT\
ATCATGCGAACAATTCAACAGACACTGTAGACACAGTACTAGAAAAGAATGTAACAGTAACACACTCTGT\
TAACCTTCTAGAAGACAAGCATAACGGGAAACTATGCAAACTAAGAGGGGTAGCCCCATTGCATTTGGGT\
AAATGTAACATTGCTGGCTGGATCCTGGGAAATCCAGAGTGTGAATCACTCTCCACAGCAAGCTCATGGT\
CCTACATTGTGGAAACACCTAGTTCAGACAATGGAACGTGTTACCCAGGAGATTTCATCGATTATGAGGA\
GCTAAGAGAGCAATTGAGCTCAGTGTCATCATTTGAAAGGTTTGAGATATTCCCCAAGACAAGTTCATGG\
CCCAATCATGACTCGAACAAAGGTGTAACGGCAGCATGTCCTCATGCTGGAGCAAAAAGCTTCTACAAAA\
ATTTAATATGGCTAGTTAAAAAAGGAAATTCATACCCAAAGCTCAGCAAATCCTACATTAATGATAAAGG\
GAAAGAAGTCCTCGTGCTATGGGGCATTCACCATCCATCTACTAGTGCTGACCAACAAAGTCTCTATCAG\
AATGCAGATGCATATGTTTTTGTGGGGTCATCAAGATACAGCAAGAAGTTCAAGCCGGAAATAGCAATAA\
GACCCAAAGTGAGGGATCAAGAAGGGAGAATGAACTATTACTGGACACTAGTAGAGCCGGGAGACAAAAT\
AACATTCGAAGCAACTGGAAATCTAGTGGTACCGAGATATGCATTCGCAATGGAAAGAAATGCTGGATCT\
GGTATTATCATTTCAGATACACCAGTCCACGATTGCAATACAACTTGTCAAACACCCAAGGGTGCTATAA\
ACACCAGCCTCCCATTTCAGAATATACATCCGATCACAATTGGAAAATGTCCAAAATATGTAAAAAGCAC\
AAAATTGAGACTGGCCACAGGATTGAGGAATATCCCGTCTATTCAATCTAGAGGCCTATTTGGGGCCATT\
GCCGGTTTCATTGAAGGGGGGTGGACAGGGATGGTAGATGGATGGTACGGTTATCACCATCAAAATGAGC\
AGGGGTCAGGATATGCAGCCGACCTGAAGAGCACACAGAATGCCATTGACGAGATTACTAACAAAGTAAA\
TTCTGTTATTGAAAAGATGAATACACAGTTCACAGCAGTAGGTAAAGAGTTCAACCACCTGGAAAAAAGA\
ATAGAGAATTTAAATAAAAAAGTTGATGATGGTTTCCTGGACATTTGGACTTACAATGCCGAACTGTTGG\
TTCTATTGGAAAATGAAAGAACTTTGGACTACCACGATTCAAATGTGAAGAACTTATATGAAAAGGTAAG\
AAGCCAGCTAAAAAACAATGCCAAGGAAATTGGAAACGGCTGCTTTGAATTTTACCACAAATGCGATAAC\
ACGTGCATGGAAAGTGTCAAAAATGGGACTTATGACTACCCAAAATACTCAGAGGAAGCAAAATTAAACA\
GAGAAGAAATAGATGGGGTAAAGCTGGAATCAACAAGGATTTACCAGATTTTGGCGATCTATTCAACTGT\
CGCCAGTTCATTGGTACTGGTAGTCTCCCTGGGGGCAATCAGTTTCTGGATGTGCTCTAATGGGTCTCTA\
CAGTGTAGAATATGTATTTAA------------------------------------------'

SC_H1_N1 = 'ATGGAGGCAAGACTACTGGTCTTGTTATGTGCATTTGCAGCTACAAATGCAGACACAATATGTATAGGCT\
ACCATGCGAATAACTCAACCGACACTGTTGACACAGTACTCGAAAAGAATGTGACCGTGACACACTCTGT\
TAACCTGCTCGAAGACAGCCACAACGGAAAACTATGTAAATTAAAAGGAATAGCCCCATTACAATTGGGG\
AAATGTAATATCGCCGGATGGCTCTTGGGAAACCCGGAATGCGATTTACTGCTCACAGCGAGCTCATGGT\
CCTATATTGTAGAAACATCGAACTCAGAGAATGGAACATGTTACCCAGGAGATTTCATCGACTATGAAGA\
ACTGAGGGAGCAATTGAGCTCAGTGTCATCGTTTGAAAAATTCGAAATATTTCCCAAGACAAGCTCGTGG\
CCCAATCATGAAACAACCAAAGGTGTAACGGCAGCATGCTCCTATGCGGGAGCAAGCAGTTTTTACAGAA\
ATTTGCTGTGGCTGACAAAGAAGGGAAGCTCATACCCAAAGCTTAGCAAGTCCTATGTGAACAATAAAGG\
GAAAGAAGTCCTTGTACTATGGGGTGTTCATCATCCGCCTACCGGTACTGATCAACAGAGTCTCTATCAG\
AATGCAGATGCTTATGTCTCTGTAGGGTCATCAAAATATAACAGGAGATTCACCCCGGAAATAGCAGCGA\
GACCCAAAGTAAGAGATCAAGCTGGGAGGATGAACTATTACTGGACATTACTAGAACCCGGAGACACAAT\
AACATTTGAGGCAACTGGAAATCTAATAGCACCATGGTATGCTTTCGCACTGAATAGAGGTTCTGGATCC\
GGTATCATCACTTCAGACGCACCAGTGCATGATTGTAACACGAAGTGTCAAACACCCCATGGTGCTATAA\
ACAGCAGTCTCCCTTTCCAGAATATACATCCAGTCACAATAGGAGAGTGCCCAAAATACGTCAGGAGTAC\
CAAATTGAGGATGGCTACAGGACTAAGAAACATTCCATCTATTCAATCCAGGGGTCTATTTGGAGCCATT\
GCCGGTTTTATTGAGGGGGGATGGACTGGAATGATAGATGGATGGTATGGTTATCATCATCAGAATGAAC\
AGGGATCAGGCTATGCAGCGGATCAAAAAAGCACACAAAATGCCATTGACGGGATTACAAACAAGGTGAA\
TTCTGTTATCGAGAAAATGAACACCCAATTCACAGCAGTGGGTAAAGAATTCAACAACTTAGAAAGAAGG\
ATAGAAAATTTAAATAAAAAAGTCGATGATGGATTTCTGGATATTTGGACATATAATGCAGAATTGTTAG\
TTCTACTGGAAAATGAAAGAACCCTGGATTTCCATGACTCAAATGTAAGGAATCTGTATGAGAAAGTAAA\
AAGCCAATTAAAGAATAATGCCAAGGAAATCGGAAATGGATGTTTTGAGTTCTACCACAAGTGTGACGAT\
GCATGCATGGAAAGTGTAAGAAATGGGACTTATGATTACCCAAAATATTCAGAAGAATCAAAGTTGAACA\
GAGAAGAAATAGATGGAGTGAAATTAGAATCAATGGGGGTCTATCAGATTCTGGCGATCTACTCAACTGT\
CGCCAGTTCACTAGTGCTGTTAGTCTCCCTGGGGGCAATCAGCTTCTGGATGTGTTCTAATGGGTCTTTG\
CAGTGCAGAATATGCATTTGA------------------------------------------'



condon_length = 3

def main():

    print(len(Brisbane_H1_N1))
    print(len(Cali_H1_N1))
    print(len(SC_H1_N1))

    sequences = [Brisbane_H1_N1,Cali_H1_N1]
    seq_names = ['Brisbane_H1_N1', 'Cali_H1_N1']

    #sequences = [Brisbane_H1_N1,Cali_H1_N1,SC_H1_N1]
    #seq_names = ['Brisbane_H1_N1', 'Cali_H1_N1','SC_H1_N1']
    protein_list = []

    for i in range(len(sequences)):
        protein_list.append(convert_bases_to_proteins(sequences[i]))


    protein_comparisons = compare_proteins(protein_list)

    display_proteins(protein_list,protein_comparisons, seq_names)


def protein_alignment(sequences, seq_names):

    protein_list = []

    for i in range(len(sequences)):

        protein_list.append(convert_bases_to_proteins(sequences[i]))


    protein_comparisons = compare_proteins(protein_list)

    display_proteins(protein_list,protein_comparisons, seq_names)


def convert_bases_to_proteins(seq):

    protein_seq = []
    codon_bases = ''
    codon = ''
    times_to_run = int(len(seq) / condon_length)

    for index in range(times_to_run):

         codon_bases = seq[0:3]

         if(codon_bases.count('-',0,len(codon_bases)) == 1 and codon_bases.endswith('-')):
             codon = try_dict(codon_bases)

         elif(codon_bases.count('-',0,len(codon_bases)) >= 1):
            codon = ' '

         else:
             codon = protein_abrv_dict.get(codon_bases)

         protein_seq.append(codon)
         seq = seq[3:]

    return protein_seq


def try_dict(codon_bases):

    posibility_A = protein_abrv_dict.get(codon_bases[0:2] + 'A')
    posibility_T = protein_abrv_dict.get(codon_bases[0:2] + 'T')
    posibility_C = protein_abrv_dict.get(codon_bases[0:2] + 'C')
    posibility_G = protein_abrv_dict.get(codon_bases[0:2] + 'G')

    if(posibility_A == posibility_G and posibility_C == posibility_T):
        codon = posibility_A

    else:
        codon = '-'

    return codon

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

def display_proteins(protein_list, protein_comparisons, seq_names):

    bad_output = True

    list_length = len(protein_comparisons)

    while bad_output:

        output_length = input("How many proteins per line would you like?: ")

        if(not output_length.isnumeric()):
            print("Please use an integer for the protein length")

        elif(int(output_length) > list_length):
            print("Please choose a shorter number")

        else:
            output_length = int(output_length)
            bad_output = not bad_output

    full_rows = list_length//output_length
    remainder_row = list_length%output_length


    if(len(seq_names) == 2):

        for i in range(full_rows):
            start_num = i * output_length
            end_num = i * output_length + output_length
            max_left = max(len(seq_names[0]), len(seq_names[1]))

            #Note the 6 is the number of spaces in the protein sequence lines
            comparison_left =  (max_left + output_length + 6 
            + len(str(start_num)))

            protein_str_0 = ''.join(protein_list[0][start_num:end_num])
            protein_str_1 = ''.join(protein_list[1][start_num:end_num])
            comparison_str = ''.join(protein_comparisons)


            print(seq_names[0].ljust(max_left) + ' '*5 +
                  str(start_num) + ' ' + protein_str_0)

            print(''+str(comparison_str[start_num:end_num]).
                  rjust(comparison_left))

            print(seq_names[1].ljust(max_left) + ' '*5 +
                  str(start_num) + ' ' + protein_str_1)

            print(' ')

        if(remainder_row != 0):
            protein_str_0 = ''.join(protein_list[0][end_num:list_length])
            protein_str_1 = ''.join(protein_list[1][end_num:list_length])
            comparison_str = ''.join(protein_comparisons)


            print(seq_names[0].ljust(max_left) + ' '*5 +
                      str(end_num) + ' ' + protein_str_0)

            comparison_left = max_left + remainder_row + 6 + len(str(start_num))
            print(''+str(comparison_str[end_num:list_length]).
                      rjust(comparison_left))

            print(seq_names[1].ljust(max_left) + ' '*5 +
                      str(end_num) + ' ' + protein_str_1)

            

    else:
        for i in range(full_rows):
            start_num = i * output_length
            end_num = i * output_length + output_length
            max_left = max(len(seq_names[0]), len(seq_names[1]))

            #Note the 6 is the number of spaces in the protein sequence lines
            comparison_left =  (max_left + output_length + 6 
            + len(str(start_num)))

        for i in range(len(protein_list)):
            2+2


if __name__ == '__main__': main()
