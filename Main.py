from FASTA import getSeq
from sys import argv
from Alignment import progressive_alignment
from Align_Tool import multi_print_alignment
from pprint import pprint

def main():
    in_file_name = input("enter the name of the file you would like to read: ")
    fasta_file = getSeq(in_file_name)
    #fasta_file = [["name1", "name2", "name3"], ["ATG", "ATAG", "TAG"]]
    choices = ""
    for i in range(len(fasta_file[0])):
        print(str(i) + " : " + fasta_file[0][i])
    choices = input("Enter the Associated numbers of the sequences you would like to analyze : ")
    arr_choices = [];
    temp = 0
    chunk = int(input("Enter the number of elements you would like to see on each line  : "))
    for i in range(len(choices)):
        if choices[i].isdigit():
            temp = (temp*10) + int(choices[i])
        elif choices[i] == " ":
            arr_choices.append(temp)
            temp = 0
    if temp != 0:
        arr_choices.append(temp)
    if len(arr_choices) < 2 :
        print("You chose one or no sequences, please choose more for an alignment")
        return
    str_to_be_align = []
    for i in arr_choices:
        print(i)
        str_to_be_align.append(fasta_file[1][i])
    align_strs = progressive_alignment(str_to_be_align)
    for i in align_strs[0]:
        print(fasta_file[0][i])
    multi_print_alignment(align_strs[1], chunk)
    return
main()
