import numpy as np
from pprint import pprint

str1 = ("GATCACAGGTCTATCACCCTATTAACCACTCACGGGAGCTCTCCATGCATTTGGTATTTTCGTCTGGGGG"
"GTGTGCACGCGATAGCATTGCGAGACGCTGGAGCCGGAGCACCCTATGTCGCAGTATCTGTCTTTGATTC"
"CTGCCTCATCCTGTTATTTATCGCACCTACGTTCAATATTACAGGCGAACATACCTACTGAAGTGTGTTA"
"ATTAATTAATGCTTATAGGACATAATAATAACAATTGAATGTCTGCACAGCCGCTTTCCACACAGACATC"
"ATAACAAAAAATTTCCACCAAACCCCCCCCTCCCCCCGCTTCTGGCCACAGCACTTAAACACATCTCTGC"
"CAAACCCCAAAAACAAAGAACCCTAACACCAGCCTAACCAGATTTCAAATTGTATCTTTTGGCGGTATGC"
"ACTTTTAACAGTCACCCCCCAACTAACACATTATTTTCCCCTCCCACTCCCATACTACTAATCTCATCAA"
"TACAACCCCCGCCCATCCTACCCAGCACACACACACCGCTGCTAACCCCATACCCCGAACCAACCAAACC"
"CCAAAGACACCCCCCACAGTTTATGTAGCTTACCTCCTCAAAGCAATACACTGAAAATGTTTAGACGGGC"
"TCACATCACCCCATAAACAAATAGGTTTGGTCCTAGCCTTTCTATTAGCTCTTAGTAAGATTACACATGC"
"AAGCATCCCCGTTCCAGTGAGTTCACCCTCTAAATCACCACGATCAAAAGGGACAAGCATCAAGCACGCA")

str2 = ("GCAATGCAGCTCAAAACGCTTAGCCTAGCCACACCCCCACGGGAAACAGCAGTGATTAACCTTTAGCAAT" 
"AAACGAAAGTTTAACTAAGCTATACTAACCCCAGGGTTGGTCAATTTCGTGCCAGCCACCGCGGTCACAC" 
"GATTAACCCAAGTCAATAGAAGCCGGCGTAAAGAGTGTTTTAGATCACCCCCTCCCCAATAAAGCTAAAA" 
"CTCACCTGAGTTGTAAAAAACTCCAGTTGACACAAAATAGACTACGAAAGTGGCTTTAACATATCTGAAC" 
"ACACAATAGCTAAGACCCAAACTGGGATTAGATACCCCACTATGCTTAGCCCTAAACCTCAACAGTTAAA"
"TCAACAAAACTGCTCGCCAGAACACTACGAGCCACAGCTTAAAACTCAAAGGACCTGGCGGTGCTTCATA"
"TCCCTCTAGAGGAGCCTGTTCTGTAATCGATAAACCCCGATCAACCTCACCACCTCTTGCTCAGCCTATA"
"TACCGCCATCTTCAGCAAACCCTGATGAAGGCTACAAAGTAAGCGCAAGTACCCACGTAAAGACGTTAGG"
"TCAAGGTGTAGCCCATGAGGTGGCAAGAAATGGGCTACATTTTCTACCCCAGAAAACTACGATAGCCCTT"
"ATGAAACTTAAGGGTCAAAGGTGGATTTAGCAGTAAACTGAGAGTAGAGTGCTTAGTTGAACAGGGCCCT"
"GAAGCGCGTACACACCGCCCGTCACCCTCCTCAAGTATACTTCAAAGGACATTTAACTAAAACCCCTACG")

str1s = "GCAATGCAGCTCAAAACGCTTAGCCTAGCCACACCCCCACGGGAAACAGCAGTGATTAACCTTTAGTAAT"
str2s = "GATCACAGGTCTATCACCCTATTAACCGCTCACGGGAGCTCTCCATGAATTTGGTATTTTCGTCTGTGGG"
str3s = "GAAGCGCGTACACACCGCCCGTCACCCGCCTCAAGTATACTTCAAAGAACATTTAACTAAAACCCCTACG"
str4s = "TACCGCCATCTTCAGCAAACCCTGATGGAGGCTACAAAGTAAGCGCAAGTACCCACGTAAAGACGTTAGG"
str5s = "TCAAGGTGTAGCCCATGAGGTGGCAAGAAATGGGCTACATTTTCTACACCAGAAAACTACGATAGCTCTT"

str_lst = [str1s, str2s, str3s, str4s, str5s]
def print_alignment(str1, str2, chunk):
    keep_going = True
    offset = 0
    while(keep_going):
        string1 = ""
        print("Base Pairs "+ str(offset) +" to " + str(min(offset + chunk, len(str1))) + ": ")
        string3 = ""
        string1 = string1 + str1[offset:min(len(str1), offset + chunk)]
        string3 = string3 + str2[offset: min(len(str2), offset+ chunk)]
        
        string2 = ""
        '''
        for i in range(len(str1)):
            string2 += " "
        '''
        for i in range(offset, offset+chunk):
            if(i >= len(str1) or i >= len(str2)):
                keep_going = False
                break
            elif(str1[i] == "-" or str2[i] == "-"):
                string2 = string2 + " "
            elif(str1[i] == str2[i]):
                string2 = string2 + "|"
            else:
                string2 = string2 + "."
        print(string1)
        print(string2)
        print(string3)
        string1 = ""
        string2 = ""
        string3 = ""
        offset = offset + chunk
    return

'''
Param: str_lst : list of aligned strings
Param: chunk : how much we want to split the string into
chunks 
'''
def multi_print_alignment(seq_lst, chunk):
    keep_going = True
    offset = 0

    string1 = ""
    string2 = ""

    star_arr = [True] * chunk

    diff_str = ""
    str1 = ""
    str2 = ""
    even = True

    if len(seq_lst) % 2 != 0:
        even = False
    #seq_count = 0

    #TODO stars at bottom if they all are same in one place
    #TODO print fasta names aka have array of 2 element as param
    while keep_going:
        print()
        #print(f"Base Pairs {offset} to {str(min(offset + chunk, len(seq_lst[0])))}: ")
        

        for i in range(len(seq_lst) - 1):
            string1 = seq_lst[i]
            if i < len(seq_lst) - 1:
                string2 = seq_lst[i + 1]

            str1 = seq_lst[i][offset : min((offset + chunk), len(seq_lst[i]))]
            str1_len = len(str1)
            if i < len(seq_lst) - 1:
                str2 = seq_lst[i + 1][offset : min((offset + chunk), len(seq_lst[i+1]))]
            
            for j in range(offset, min((offset + chunk), len(string1))):
                #print(j)
                if(string1[j] == "-" or string2[j] == "-"):
                    diff_str += " "
                elif(string1[j] == string2[j]):
                    diff_str += "|"
                else: 
                    diff_str +=  "."
                    star_arr[j - offset] = False
                    


            if even or i == 0:
                print(str1)
            print(diff_str)
            if even or i == len(seq_lst) - 1 :
                print(str2)
            even = not even # need to flip this every other iteration             
            string1 = string2 = str1 = str2 = diff_str = ""
        
        if len(seq_lst) % 2 == 0:
            even = not even
        offset += chunk
        for b in range(len(star_arr)):
            if b < str1_len:
                if star_arr[b]:
                    print('*', end='')
                else: 
                    print(' ', end='')
        star_arr = [True] * chunk
        if offset > len(seq_lst[0]): 
            keep_going = False

def basic_multi_string_print(string_arr , chunk):
    posInString = [0 for i in range(len(string_arr))]
    outString = ""
    file = open("/log/out.txt" , "w")

#print_alignment(str1, str2, 70)
#pprint(e_list)
#multi_print_alignment(e_list, 40)
