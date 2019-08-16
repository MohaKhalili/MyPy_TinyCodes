#  a function that takes a list of words as an input argument and
#  returns True if the list is sorted and returns False otherwise.
def Sorted_Test(String):
    result = False
    new_String = sorted(String)
    if new_String == String:
        result = True
    return result

# driver code test
vowels = ['eraee', 'amin', 'umberella', 'omid', 'ida','abi']
#vowels = ['abi', 'amin', 'eraee', 'ida', 'omid', 'umberella']

result = Sorted_Test(vowels)
print(result)