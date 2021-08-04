
#--------FILE1-TAGGING--------(tagging all lines in LP7 with file 1 for easy tracking)
string_to_add_for_file1 = "(FILE1)"
file1 = ("DL_UASM_LP7.mgf")
with open(file1, 'r') as f:
    file_lines = [''.join(  [string_to_add_for_file1, x.strip(),'\n']    ) for x in f.readlines()]

with open(file1, 'w') as f:
    f.writelines(file_lines)

#--------FILE2-TAGGING--------(tagging all lines in LP8 with file 2 for easy tracking)
string_to_add_for_file2 = "(FILE2)"
file2 = ("DL_UASM_LP8.mgf")
with open(file2, 'r') as f:
    file_lines = [''.join(  [string_to_add_for_file2, x.strip(),'\n']    ) for x in f.readlines()]

with open(file2, 'w') as f:
    f.writelines(file_lines)

#--------FILE3-TAGGING--------(tagging all lines in LP9 with file 3 for easy tracking)
string_to_add_for_file3 = "(FILE3)"
file3 = ("DL_UASM_LP9.mgf")
with open(file3, 'r') as f:
    file_lines = [''.join(  [string_to_add_for_file3, x.strip(),'\n']    ) for x in f.readlines()]

with open(file3, 'w') as f:
    f.writelines(file_lines)

#--------MERGE-FILES--------(merging LP7,LP8, and LP9 into one file with the file tags)
combofile = ["DL_UASM_LP7.mgf", "DL_UASM_LP8.mgf", "DL_UASM_LP9.mgf"]
with open('DL_LP789_CombinedFile', 'w') as outfile:
    for fname in combofile:
        with open(fname) as infile:
            outfile.write(infile.read())

#--------SORTING-M/Z--------

 
