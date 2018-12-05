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
str5 = "ATAG"
str6 = "ATG"

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
                temp = get_dynamic_score(str_arr[i], str_arr[c])
                if maxi < temp:
                    maxi = temp
                    str1 = i
                    str2 = c
    ret = {str1,str2}
    return ret

                
            


#print_alignment(str1, str2, 70)
#pprint(str_lst)
#multi_print_alignment(str_lst, 30)
out = twoStringAlign(str6,str5)
print(out)
print(out[0][out[2][0]:out[2][0]+1])
str3 = "ABC"
str3 = str3[:out[2][0]] + "-" + str3[out[2][0]:]
print(str3)
