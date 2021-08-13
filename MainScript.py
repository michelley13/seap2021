#--------FILE1-TAGGING--------Adding a specific text to the first file that the user inputs 

string_to_add_for_file1 = "(FILE1)" #the specific text can be changed for any of the files       #assigning the specific words to be added as the tag for the first file
file1 = input("Please enter the exact name of the FIRST file you would like to tag: ")#asking the user to input the first file that they would like to tag and assignning that to a variable
with open(file1, 'r') as f:
    file_lines = [''.join(  [string_to_add_for_file1, x.strip(),'\n']    ) for x in f.readlines()] #ensures that every line in the code is tagged

with open(file1, 'w') as f:
    f.writelines(file_lines) #tags the code with the correct string to add


#--------FILE2-TAGGING--------Adding a specific text to the second file that the user inputs 
string_to_add_for_file2 = "(FILE2)"             #assigning the specific words to be added as the tag for the second file
file2 = input("Please enter the exact name of the SECOND file you would like to tag: ")#asking the user to input the second file that they would like to tag and assignning that to a variable
with open(file2, 'r') as f:
    file_lines = [''.join(  [string_to_add_for_file2, x.strip(),'\n']    ) for x in f.readlines()] #ensures that every line in the code is tagged 

with open(file2, 'w') as f:
    f.writelines(file_lines) #tags the code with the correct string to add

#--------FILE3-TAGGING--------Adding a specific text to the third file that the user inputs 
string_to_add_for_file3 = "(FILE3)"           #assigning the specific words to be added as the tag for the third file           
file3 = input("Please enter the exact name of the THIRD file you would like to tag: ") #asking the user to input the third file that they would like to tag and assignning that to a variable
with open(file3, 'r') as f:
    file_lines = [''.join(  [string_to_add_for_file3, x.strip(),'\n']    ) for x in f.readlines()] #ensures that every line in the code is tagged

with open(file3, 'w') as f:
    f.writelines(file_lines) #tags the code with the correct string to add
 
#--------MERGE-FILES--------
combofile = [file1, file2, file3]  #creating a variable that includes all the tagged files to be combined
with open('CombinedFile', 'w') as outfile: #creating a new file called ComboFile 
    for fname in combofile:
        with open(fname) as infile:
            outfile.write(infile.read()) #adding all the lines of each file to the combo file
