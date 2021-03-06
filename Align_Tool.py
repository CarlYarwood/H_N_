'''
Align_Tool.py - This file holds all the necessary code for 
visualising alignment

Eli Charleville 

December 10 2018
'''


from pprint import pprint
'''
print_alignment -prints the aligned for two strings of sequences

Param: str1 : first string we want to visualize
Param: str2 : second string we want to visualize

Returns: Nothing
'''
def print_alignment(str1, str2, chunk):
    keep_going = True
    offset = 0
    total_align = 0
    while(keep_going):
        string1 = ""
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
                total_align += 1
            else:
                string2 = string2 + "."
        print(string1)
        print(string2)
        print(string3)
        print()
        string1 = ""
        string2 = ""
        string3 = ""
        offset = offset + chunk
    print("percent align is : "+ str((total_align/len(str1))))
    return

'''
multi_print_alignment - takes in a list of strings and prints a multi
string alignment visualisation

Param: str_lst : list of aligned strings
Param: chunk : how much we want to split the string into
chunks 

Returns: Nothing
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
    while keep_going:
        print()
        
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



'''
simple_multi_sequence_output - Does the same as multi_print_alignment
but does not have "|" or "." to tell us where the sequences differ

Param: str_arr : array of sequences we want to visualise 
Param: chunck : how many characters we eant to see per line 
in the visualisations 

Returns: Nothing
'''
def simple_multi_sequence_output(str_arr, chunk):
    if(len(str_arr) == 2):
        print_alignment(str_arr[0], str_arr[1], chunk)
        return
    current_pos = 0
    keep_going = True
    total_align = 0
    while(keep_going):
        line = ""
        for c in range(current_pos, min(len(str_arr[0]), current_pos + chunk)):
            expected_char = str_arr[0][c]
            string_char = "*"
            total_align += 1
            Again = False
            for z in range(len(str_arr)):
                if str_arr[z][c] != expected_char:
                   string_char = " "
                   if not Again:
                       total_align -= 1
                       Again = True
                elif str_arr[z][c] == "-":
                    string_char = " "
                    if not Again :
                        total_align -= 1
                        Again = True
            line += string_char
        for i in range(len(str_arr)):
            print(str_arr[i][current_pos:min(len(str_arr[i]), current_pos + chunk)])
        print(line)
        if(current_pos > len(str_arr[0])):
            keep_going = False
        current_pos += chunk
    print("percent alingment is: " + str((total_align/len(str_arr[0]))))
    return