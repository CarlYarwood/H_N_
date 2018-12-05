import numpy as np
from pprint import pprint


gap_penalty = -7
match_penalty = -4
match_reward = 5
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

str1s = "GCAATGCAGCTCAAAACGCTTAGCCTAGCCACACCCCCACGGGAAACAGCAGTGATTAACCTTTAGCAAT"
str2s = "GATCACAGGTCTATCACCCTATTAACCGCTCACGGGAGCTCTCCATGAATTTGGTATTTTCGTCTGGGGG"
str3s = "GAAGCGCGTACACACCGCCCGTCACCCGCCTCAAGTATACTTCAAAGAACATTTAACTAAAACCCCTACG"
str4s = "TACCGCCATCTTCAGCAAACCCTGATGGAGGCTACAAAGTAAGCGCAAGTACCCACGTAAAGACGTTAGG"
str5s = "TCAAGGTGTAGCCCATGAGGTGGCAAGAAATGGGCTACATTTTCTACACCAGAAAACTACGATAGCCCTT"
str_lst = [str1s, str2s, str3s, str4s]
def twoStringAlign( str1, str2 ):
    workstr1 = "-" + str1
    workstr2 = "-" + str2
    match_arr = np.zeros( ( len( workstr1 ), len( workstr2 ) ) )
    for index in range( len( workstr1 ) ):
        match_arr[ index ][ 0 ] = index * gap_penalty
    for index in range( len(workstr2)):
        match_arr[0][index] = index * gap_penalty
        
    for row in range( len( workstr1 ) - 1 ):
        for col in range( len( workstr2 ) - 1 ):
            possibleChoices = [( match_arr[ row ][ col + 1 ] + gap_penalty ),
                               ( match_arr[ row + 1 ][ col ] + gap_penalty ),
                               ( ( match_arr[ row ][ col ] + match_reward )
							   if
                               ( workstr1[ row + 1 ] == workstr2[ col + 1 ])
                               else( match_arr[ row ][ col ] + match_penalty
							   ))]
            match_arr[ row + 1 ][ col + 1 ] = max( possibleChoices )
    return  traceBack(match_arr, workstr1, workstr2)
def traceBack(dynamicArray, str1, str2):
    keepGoing = True
    row = len(str1) - 1
    col = len(str2) - 1
    newStr1 = ""
    newStr2 = ""
    editPlacesRow = []
    while(keepGoing):
        if ((str1[row] == str2[col]) and (dynamicArray[row - 1][col - 1] == dynamicArray[row][col] - 5)) or((str1[row] != str2[col]) and (dynamicArray[row -1][col - 1] == dynamicArray[row][col] + 4)):
            newStr1 = str1[row] + newStr1
            newStr2 = str2[col] + newStr2
            row = row - 1
            col = col - 1
        elif dynamicArray[row - 1][col] == dynamicArray[row][col] + 7:
            newStr1 = str1[row] + newStr1
            newStr2 = "-" + newStr2
            row = row - 1
        elif dynamicArray[row][col - 1] == dynamicArray[row][col] + 7:
            newStr1 = "-" + newStr1
            newStr2 = str2[col] + newStr2
            col = col -1
            editPlacesRow.append(row)
        if row == 0 and col == 0:
            keepGoing = False
    ret = [newStr1, newStr2, editPlacesRow]
    return ret
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
    #seq_count = 0

    #TODO stars at bottom if they all are same in one place
    #TODO print fasta names aka have array of 2 element as param
    while keep_going:
        print()
        print(f"Base Pairs {offset} to {str(min(offset + chunk, len(seq_lst[0])))}: ")
        

        for i in range(len(seq_lst) - 1):
            string1 = seq_lst[i]
            if i < len(seq_lst) - 1:
                string2 = seq_lst[i + 1]

            str1 = seq_lst[i][offset : min((offset + chunk), len(seq_lst[i]))]
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
                    


            if even:
                print(str1)
            print(diff_str)
            if even:
                print(str2)
            even = not even # need to flip this every other iteration             
            string1 = string2 = str1 = str2 = diff_str = ""

        even = not even #TODO test on odd numbered lists 
        offset += chunk
        for b in range(len(star_arr)):
            if b < len(str1):
                if star_arr[b]:
                    print('*', end='')
                else: 
                    print(' ', end='')
        star_arr = [True] * chunk
        if offset > len(str_lst[0]): 
            keep_going = False
    



def get_dynamic_score(str1, str2):
    workstr1 = "-" + str1
    workstr2 = "-" + str2
    match_arr = np.zeros( ( len( workstr1 ), len( workstr2 ) ) )
    for index in range( len( workstr1 ) ):
        match_arr[ index ][ 0 ] = index * gap_penalty
    for index in range( len(workstr2)):
        match_arr[0][index] = index * gap_penalty
        
    for row in range( len( workstr1 ) - 1 ):
        for col in range( len( workstr2 ) - 1 ):
            possibleChoices = [( match_arr[ row ][ col + 1 ] + gap_penalty ),
                               ( match_arr[ row + 1 ][ col ] + gap_penalty ),
                               ( ( match_arr[ row ][ col ] + match_reward )
							   if
                               ( workstr1[ row + 1 ] == workstr2[ col + 1 ])
                               else( match_arr[ row ][ col ] + match_penalty
							   ))]
            match_arr[ row + 1 ][ col + 1 ] = max( possibleChoices )
    return  match_arr[len(str1)-1][len(str2)-2]
def get_indexes_for_best_alignment(str_arr):
    str1 = 0
    str2 = 1
    maxi = get_dynamic_score(str_arr[0], str_arr[1])
    for i in range(len(str_arr)):
        for c in range(i, len(str_arr)):
            if i != c:
                temp = get_dynamic_score(str_arr[i], str_arr[c]):
                if maxi < temp:
                    maxi = temp
                    str1 = i
                    str2 = c
    ret = {str1,str2}
    return ret

                
            


#print_alignment(str1, str2, 70)
pprint(str_lst)
multi_print_alignment(str_lst, 30)
