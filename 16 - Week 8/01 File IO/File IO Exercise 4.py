# A function that accepts a filename as input argument, the file 
# contains the information about a persons expenses on milk and 
# bread and returns a dictionary that contains exactly the strings 
# 'milk' and 'bread' as the keys and their floating point values 
# in a list as values. Each line of the file may start with a 'm' 
# or a 'b' denoting milk or bread respectively. For example if the 
# contents of the file are:

# m 0 0 0
# b 2 5 1
# b 3 5 4
# m 1 0 0
# b 5 3 1
# m 0 1 0
# b 2 4 5
# then your function should return a dictionary such as:
# out_dict = {'milk': [[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]], 
#             'bread': [[2.0, 5.0, 1.0], [3.0, 5.0, 4.0], [5.0, 3.0, 1.0], [2.0, 4.0, 5.0]]}

################### Sample Solution ###################
def dict_milk_bread(file_name):
    my_file = open(file_name,'r')
    data = my_file.readlines()
    my_file.close()
    out_dict = {}
    milk_list = []
    bread_list = []
    for item in data:
        name, person1, person2, person3 = item.strip().split(' ')
        if name == 'm':
            milk_list.append([float(person1), float(person2), float(person3)])
        else:
            bread_list.append([float(person1), float(person2), float(person3)])
    out_dict['milk'] = milk_list
    out_dict['bread'] = bread_list
    return out_dict

################### Driver Code Tester ###################
file_directory = '.\\16 - Week 8\\01 File IO\File IO Exercise 4.csv'
result = dict_milk_bread(file_directory)
print(result)

################### Sample Solution ###################
def _construct_nested_list_from_file_sample_(filename):
    my_dictionary = {}
    my_dictionary["milk"] = []
    my_dictionary["bread"] = []
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open(filename, mode)
    data = file_pointer.readlines()
    for line in data:
        first_character = line[0]      
        # remove the first character and
        # strip and split by white space
        items = line[1::].strip().split()
        # change the string items into floats
        # The line below is an example of doing it by list comprehensions
        # float_items = [float(x) for x in items] 
    	float_items=[]
    	for current_item in items:
    		float_items.append(float(current_item))
    	if first_character == "m":	
            my_dictionary["milk"] += [float_items]
        if first_character == "b":
            my_dictionary["bread"] += [float_items]
    return my_dictionary