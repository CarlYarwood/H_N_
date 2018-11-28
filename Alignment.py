import numpy as np

gap_penalty = -7
match_penalty = -4
match_reward = 5
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
def PrintAlignment(str1, str2, chunk):
    keepGoing = True
    offset = 0
    while(keepGoing):
        string1 = "Base Pairs "+ str(offset) +" to " + str(min(offset + chunk, len(str1)))
        string3 = "Base Pairs "+ str(offset) +" to " + str(min(offset + chunk, len(str2)))
        string1 = string1 + str1[offset:min(len(str1), offset + chunk)]
        string3 = string3 + str2[offset: min(len(str2), offset+ chunk)]
        offset = offset + chunk
        string2 = ""
        for i in range(len(str1)):
            string2 = string2 + " "
        for i in range(offset, offset+chunk):
            if(i >= len(str1) or i >= len(str2)):
                keepGoing = False
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
    return
