#  a function that accepts a dictionary as input and returns a
#  sorted list of all the keys in the dictionary.

def Sorted_Keys(your_dict):
    keys = your_dict.keys()
    keys = list(keys)
    keys.sort()
    return keys

# driver code tester
my_dict = {'name':'moha', 'age':'27', 'location':'qazvin'}
result = Sorted_Keys(my_dict)
print(result)
