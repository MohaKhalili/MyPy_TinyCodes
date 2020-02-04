# A function that accepts a dictionary as input and returns 
# a tuple of tuples. That is your first tuple should be the 
# tuple of all the keys, and the second tuple should be tuple 
# of all the values in the dictionary. For example if the 
# input dictionary is:

# input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"} 
# then you should return a tuple(tuple of keys, tuple of values) such as:
# ((1, 2, 3, 4), ('a', 'b', 'c', 'd'))

################### My Solution ###################
def Dictionary_to_Tuple(my_dict):

    key_list = my_dict.keys()
    value_list = my_dict.values()

    return (tuple(key_list), tuple(value_list))

################### Driver code tester ###################
input_dictionary = {1:"a", 2:"b", 3:"c", 4:"d"}
result = Dictionary_to_Tuple(input_dictionary)
print(result)