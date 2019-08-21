# a function that takes a string as input argument and returns
# a dictionary of letter counts i.e. the keys of this dictionary
# should be individual letters and the values should be the total
# count of those letters. You should ignore white spaces and they
# should not be counted as a character. Also note that a small
# letter character is equal to a capital letter character.

def Dictionary_of_Letter_Count(your_string):
    your_string = your_string.upper()
    return your_string


# driver code tester
string = "SALAM mohammad"
result = Dictionary_of_Letter_Count(string)
print(result)