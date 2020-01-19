# A function named find_longest_word that receives a string as parameter 
# and returns the longest word in the string. Assume that the input to this 
# function is a string of words consisting of alphabetic characters that are 
# separated by space(s). In case of a tie between some words return the last 
# one that occurs.

# Type your code here
def find_longest_word(some_string):
    some_string = some_string.split()
    longest_word = some_string[0]

    for i in range(1, len(some_string)):
        if len(some_string[i]) >= len(longest_word):
            longest_word = some_string[i]
    return longest_word

# driver code tester
String = input("Please enter your string : ")
result = find_longest_word(String)
print(result)

################### Instructor function ###################
# def _longest_word_sample_(input_string):
#     # Create a list of strings by splitting the original string
#     splitted_string = input_string.split()
#     # First arbitrarily set the maximum length
#     # as the length of the first string
#     maximum_length = len(splitted_string[0])
#     # Also set the longest word as the first string
#     longest_word = splitted_string[0]
#     # Go through each string in the list we created
#     # calculate the length of each string
#     # check to see if its length is larger than maximum length
#     # if so update it and return the string
#     for string in splitted_string:
#         # check the length of each string   # it resets for each string
#         string_length = len(string)
#         if string_length >= maximum_length:
#             # maximum_length = string_length
#             longest_word = string
#     return longest_word