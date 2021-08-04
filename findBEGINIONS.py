file1 = "LPshort7"

#with open(file1, 'r') as f :
#    lines = f.readlines()
#    f.close()


#-------------FIND BEGIN IONS-------------
findbegintext = "*BEGIN*IONS"

beginflag = 0 
beginindex= 0

for beginline in file1:
    beginindex += 1

    if findbegintext in beginline:
        beginflag = 1
        break
    
if beginflag == 0:
    print("string", findbegintext, "not found")

else:
    print("String", findbegintext, "found in line", beginindex)


#-------------FIND END IONS-------------
findendtext = "*END*IONS"

endflag = 0 
endindex = 0

for endline in file1:
    endindex += 1

    if findendtext in endline:
        endflag = 1
        break
    
if endflag == 0:
    print("string", findendtext, "not found")

else:
    print("String", findendtext, "found in line", endindex)


length_data = endindex - beginindex

print("The length of data set 1 is " + str(length_data))

#-------------PRINT SINGLE LINE-------------

#lines_to_print = [beginindex, endindex]

#content = file1.readlines()
#print(content)

#print(lines_to_print)


#-------------LIST OF LINES WITH BEGIN ION-------------

string_to_search = "BEGIN IONS"

def search_string_in_file(DL_UASM_LP7, string_to_search):
    """Search for the given string in file and return lines containing that string,
    along with line numbers"""
    line_number = 0
    list_of_results = []

    with open(DL_UASM_LP7,"r") as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number,line.rstrip()))

    return list_of_results        




