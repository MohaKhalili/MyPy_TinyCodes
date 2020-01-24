# A function named return_keys which accepts a dictionary and an integer as 
# input and returns an ascending sorted list of all the keys whose values 
# contain the input integer. Note that the keys of this dictionary are strings 
# while the values of this dictionary are 1 Dimensional lists of integers. For 
# example if the input dictionary is:

# sample_dictionary = {"rabbit" : [1, 2, 3],
#           "kitten" : [2, 2, 6],
#           "lioness": [6, 8, 9]}

# if your function is called as return_keys(sample_dictionary,2) , then your function should return:
# [ "kitten", "rabbit",]
# If the input integer is not found then your function should return an empty list.

# Type your code here
def Value_Containing_Key(my_dict, num):
    dict_values = list(my_dict.values())
    dict_keys = list(my_dict.keys())
    output_list = []
    for index in range(len(dict_values)):
        if num in dict_values[index]:
            output_list.append(dict_keys[index])
    return sorted(output_list)

sample = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}

num = int(input("Please enter the number : "))
result = Value_Containing_Key(sample, num)
print(result)
