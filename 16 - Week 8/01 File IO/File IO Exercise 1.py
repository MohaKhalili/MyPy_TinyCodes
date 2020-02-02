# A function that accepts a filename as input argument and reads the 
# file and saves each line of the file as an element in a list 
# (without the new line ("\n")character) and returns the list. 
# Each line of the file has comma separated values: 

# For example if the content of the file looks like this:

# Lucas,Turing,22
# Alan,Williams,27
# Layla,Trinh,21
# Brayden,Huang,22
# Oliver,Greek,20

# then your function should return a list such as
# ['Lucas,Turing,22', 'Alan,Williams,27', 'Layla,Trinh,21', 
# 'Brayden,Huang,22', 'Oliver,Greek,20']

# Please read the "File I/O Exercise Notes" before you attempt to write code.
# The first few lines of the code is there to help you!

################### My Solution ###################
def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    file_pointer.close()
    output_list = []
    for item in data:
        item = item.replace("\n","")
        output_list.append(item)
    return output_list

################### Driver Code Tester ###################
file_directory = '.\\16 - Week 8\\01 File IO\File IO Exercise 1.txt'
result = list_from_file(file_directory)
print(result)

################### Sample Solution ###################
def _construct_list_from_file_sample_(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    out_list = []
    for line in data:
        stripped_line = line.strip('\n')
        out_list.append(stripped_line)
    return out_list