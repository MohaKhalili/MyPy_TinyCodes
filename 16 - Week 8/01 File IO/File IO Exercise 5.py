# A function that accepts a file name as input argument and constructs and returns a 
# nested dictionary from it. The keys of this dictionary should be last names, and the 
# values should be dictionaries that contain first names as the keys and integer ages 
# as the values. Note that the data may contain multiple people with the same last name, 
# but it will have unique first names. Ignore any lines that start with '#' The file will 
# contain comma separated values (CSV) For example if the contents of the file are:

# #first_name,last_name,age
# Matthew,Abbey,65
# Chloe,Orion,49
# Yohaan,Adams,54
# Krishna,Adams,35
# Resa,Orion,86
# Lucas,Abbey,60
# Courtney,Abbey,67
# Joseph,Orion,45
# Mark,Abbey,60
# Eva,Orion,76

# then your function should return a dictionary such as:
# {'Abbey': {'Matthew': 65, 'Courtney': 67, 'Lucas': 60, 'Mark': 60},
#  'Orion': {'Chloe': 49, 'Resa': 86, 'Eva': 76, 'Joseph': 45},
#  'Adams': {'Krishna': 35, 'Yohaan': 54}}

################### My Solution ###################
def dect_ages(file_name):
    my_file = open(file_name,'r')
    data = my_file.readlines()
    my_file.close()
    
    out_dict = {}
    for item in data:
        if item[0] != '#':
            name, family, age = item.strip().split(',')
            my_dict = out_dict.setdefault(family, {name:int(age)})
            my_dict.update({name:int(age)})
            out_dict.setdefault(family, my_dict)
    return out_dict

################### Driver Code Tester ###################
file_directory = '.\\16 - Week 8\\01 File IO\File IO Exercise 5.csv'
result = dect_ages(file_directory)
print(result)

################### Sample Solution ###################
def _construct_nested_dictionary_from_file_sample_(filename):
    my_dictionary = {}
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open(filename, mode)
    data = file_pointer.readlines()
    for line in data:
        if line[0] != "#":
            # Split the line with the delimiter comma (',')
            first_name, last_name, age = line.strip().split(',')
            if last_name not in my_dictionary:
                my_dictionary[last_name] = {first_name: int(age)}
            else:
                if first_name not in my_dictionary[last_name]:
                    my_dictionary[last_name][first_name] = int(age)

    return my_dictionary