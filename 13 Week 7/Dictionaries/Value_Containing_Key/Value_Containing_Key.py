# a function named return_keys which accepts a dictionary and an
# integer as input and returns an ascending sorted list of all the
# keys whose values contain the input integer. Note that the keys
# of this dictionary are strings while the values of this dictionary
# are 1 Dimensional lists of integers.
def Value_Containing_Key(sample_dictionary, sample_value):
    my_list = []
    keys = sample_dictionary.keys()
    keys = list(keys)
    for k in keys:
        each_list = sample_dictionary[k]
        for index in range(len(each_list)):
            if each_list[index] == sample_value:
                my_list.append(k)
                break
    my_list.sort()
    return my_list

# driver code tester
my_dict = {'moha':[32, 54 , 102], 'amir':[78, 88, 91], 'morteza':[78, 78, 78]}
number = 78
result = Value_Containing_Key(my_dict,number)
print(result)

################### Sample Solution ###################
#def _return_keys_list_sample_(sample_dictionary, sample_value):
#    keys_list = []
#    for each_key in sample_dictionary.keys():
#        if sample_value in sample_dictionary[each_key]:
#             keys_list.append(each_key)
#    keys_list.sort()
#    return keys_list