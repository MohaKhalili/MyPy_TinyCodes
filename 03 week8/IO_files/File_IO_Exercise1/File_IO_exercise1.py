# a function that accepts a filename as input argument and reads
# the file and saves each line of the file as an element in a list
# (without the new line ("\n")character) and returns the list. Each
# line of the file has comma separated values

def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    print(data)
    # NOW CONTINUE YOUR CODE FROM HERE!!!
    my_list = []
    for line in data:
        stripped_line = line.strip('\n')
        my_list.append(stripped_line)
    return my_list


# driver code tester
result = list_from_file('File_IO_exercise1.txt')
print(result)