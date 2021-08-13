# This file's purpose is to describe what I was working on and where someone could pick up on my work. 
# What I wanted to do next is to add an option for users to enter in how many files they want to use and label them accordingly. 
#My code right now is hard coded for only 3 files, and if a user has less than or more than three files, they run into a bit of an isssue. 
#My code for this file is meant to be changed as it was a work in progress.


filenum = int(input("How many files would you like to tag:"))

for x in range(int(filenum)):
    file_counter = 1
    string_to_add_for_file1 = "(FILE" + file_counter + ")"            #
    file1 = input("Please enter the exact name of the FIRST file you would like to tag: ")
    with open(file1, 'r') as f:
        file_lines = [''.join(  [string_to_add_for_file1, x.strip(),'\n']    ) for x in f.readlines()]

    with open(file1, 'w') as f:
        f.writelines(file_lines)
