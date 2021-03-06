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
'''
Takes in and alings two strings
Arguments: two strings which will be alligned
Return: the two alligned strings and an array of numbers telling where the
the first string was modified
'''
def two_string_align( str1, str2 ):
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
'''
takes in a score matrix and two strings and does a trace back on the matrix to
align the two strings
Arguments: the score Matrix, string 1, string 2
Return: an array containing alinged string 1, aligned string 2, array of numbers
reptresenting the locations where string 1 was changed
'''
def traceBack(dynamicArray, str1, str2):
    keepGoing = True
    row = len(str1) - 1
    col = len(str2) - 1
    newStr1 = ""
    newStr2 = ""
    editPlacesRow = []
    while(keepGoing):
        #cutting this code to multiple lines drastically reduces readability
        #determiningh how to trace back
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
    #added space to help differentiat returns in main
    ret = [newStr1, newStr2, editPlacesRow, " "]
    return ret



'''
gets the alignment score of two strings using dynamic programming
Arguments: string 1, string 2
Return: an int representing how well they align
'''

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
    return  match_arr[len(str1)-1][len(str2)-1]
'''
gets indexes for best alingment
Argument:str_arr
Return: set of two integers representing the best alignment
'''
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
'''
does a progressive alingment on the strings you pass into it
Argument: array of stings to be aligned, array of ints representing choices
return: alligned strings, array of ints in order corresponding to the strings
'''
def progressive_alignment(str_arr, possible_choice_arr):
    #detemines if a two string alingment should be done
    if len(str_arr) == 2:
        return two_string_align(str_arr[0], str_arr[1])
    prev = []
    choices = []
    str_pos_1 = 0;
    str_pos_2 = 1;
    out = []
    ret = []
    scores =[]
    #determines initial pair
    print("determining initiail pair")
    best_match_val = get_dynamic_score(str_arr[0], str_arr[1]);
    for i in range(len(str_arr)):
        for c in range(i,len( str_arr)):
            if i != c :
                print("making progress")
                temp = get_dynamic_score(str_arr[i], str_arr[c])
                if temp > best_match_val:
                    best_match_val = temp
                    str_pos_1 = i
                    str_pos_2 = c
    print("Alinging initial Pair")
    scores.append(temp)
    out = two_string_align(str_arr[str_pos_1], str_arr[str_pos_2])
    prev.append(out[0])
    choices.append(possible_choice_arr[str_pos_1])
    choices.append(possible_choice_arr[str_pos_2])
    possible_choice_arr.pop(max(str_pos_1, str_pos_2))
    possible_choice_arr.pop(min(str_pos_1, str_pos_2))
    str_arr.pop(max(str_pos_1, str_pos_2))
    str_arr.pop(min(str_pos_1, str_pos_2))
    more_to_align = True
    while(more_to_align):
        consensus_string = out[1]
        str_pos_to_use = 0
        print("choosing next seq")
        best_match_val = get_dynamic_score(consensus_string, str_arr[0])
        for i  in range(len(str_arr)):
            print("making progress")
            temp = get_dynamic_score(consensus_string, str_arr[i])
            if temp > best_match_val:
                best_match_val = temp
                str_pos_to_use = i
        out = two_string_align(consensus_string, str_arr[str_pos_to_use])
        for i in range(len(prev)):
            for c in out[2]:
               prev[i] = prev[i][:c] + "-" + prev[i][c:]
        scores.append(best_match_val)
        choices.append(possible_choice_arr[str_pos_to_use])
        possible_choice_arr.pop(str_pos_to_use)
        prev.append(out[0])
        str_arr.pop(str_pos_to_use)
        if(len(str_arr) == 0):
            more_to_align = False
    prev.append(out[1])
    ret.append(choices)
    ret.append(prev)
    ret.append(scores)
    return ret

    
                
            


#print_alignment(str1, str2, 70)
#pprint(str_lst)
#multi_print_alignment(str_lst, 30)
#str_arr = ["ATG", "ATAG","AATAAAG","AATUUUUG"]

#new_str_arr = progressive_alignment(str_arr)
#for i in new_str_arr:
#    print(i)
