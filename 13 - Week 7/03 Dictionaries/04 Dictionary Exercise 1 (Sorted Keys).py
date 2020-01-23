# A function that accepts a dictionary as input and returns a sorted list 
# of all the keys in the dictionary.

# Type your code here
def Sorted_Keys(your_dict):
    return list(sorted(your_dict.keys()))

# driver code tester
my_dict = {'name':'moha', 'sex':'male', 'age':28}
result = Sorted_Keys(my_dict)
print(result)