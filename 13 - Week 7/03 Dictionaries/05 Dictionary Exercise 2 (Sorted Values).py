# A function that accepts a dictionary as input and returns a sorted 
# list of all the values in the dictionary. Assume that the values of 
# this dictionary are just integers.

# Type your code here
def Sorted_Values(your_dict):
    return sorted(list(your_dict.values()))

# driver code tester
my_dict = {'James': 19, 'Tina': 35, 'Sam': 17}
result = Sorted_Values(my_dict)
print(result)