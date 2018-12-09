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

condon_length = 3

def main():

    seq1 = 'ATGTTTAAACG-C--'
    seq2 = 'ATGTTTTTTCGAC--'

    protein_seq1 = convert_bases_to_proteins(seq1)
    protein_seq2 = convert_bases_to_proteins(seq2)

    print(protein_seq1)
    print(protein_seq2)


def convert_bases_to_proteins(seq):

    protein_seq = []
    codon_bases = ''
    codon = ''
    times_to_run = int(len(seq) / condon_length)

    for index in range(times_to_run):

         codon_bases = seq[0:3]

         if( '-' in codon_bases and
             codon_bases.count('-',0,len(codon_bases)) == 1): 
             codon = try_dict(codon_bases)
             
         elif(codon_bases.count('-',0,len(codon_bases)) > 1):
            codon = '-'
            
         else:
             codon = protein_abrv_dict.get(codon_bases)

         protein_seq.append(codon)     
         seq = seq[3:]

    return protein_seq


def try_dict(codon_bases):

    index = codon_bases.index('-')

    if(index == 0):

        posibility_A = protein_abrv_dict.get('A' + codon_bases[1:3])
        posibility_T = protein_abrv_dict.get('T' + codon_bases[1:3])
        posibility_C = protein_abrv_dict.get('C' + codon_bases[1:3])
        posibility_G = protein_abrv_dict.get('G' + codon_bases[1:3])

        if(posibility_A == posibility_G and posibility_C == posibility_T):
            codon = posibility_A 
        else:
            codon = '-'

    elif(index == 1):
        
        posibility_A = protein_abrv_dict.get(codon_bases[0] + 'A' + codon_bases[2])
        posibility_T = protein_abrv_dict.get(codon_bases[0] + 'T' + codon_bases[2])
        posibility_C = protein_abrv_dict.get(codon_bases[0] + 'C' + codon_bases[2])
        posibility_G = protein_abrv_dict.get(codon_bases[0] + 'G' + codon_bases[2])

        if(posibility_A == posibility_G and posibility_C == posibility_T):
            codon = posibility_A 
        else:
            codon = '-'
            
    else:
        posibility_A = protein_abrv_dict.get(codon_bases[0:2] + 'A')
        posibility_T = protein_abrv_dict.get(codon_bases[0:2] + 'T')
        posibility_C = protein_abrv_dict.get(codon_bases[0:2] + 'C')
        posibility_G = protein_abrv_dict.get(codon_bases[0:2] + 'G')

        if(posibility_A == posibility_G and posibility_C == posibility_T):
            codon = posibility_A 
        else:
            codon = '-'

    return codon
    
if __name__ == '__main__': main()
