# a function that accepts a dictionary as input and returns a
# sorted list of all the values in the dictionary.
def Sorted_Values(your_dict):
    values = your_dict.values()
    values = list(values)
    values.sort()
    return values

# driver code tester
my_dict = {'height':183, 'weight':80, 'age':27}
result = Sorted_Values(my_dict)
print(result)