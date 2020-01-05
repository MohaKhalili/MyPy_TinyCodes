# A function that accepts a string of words separated by spaces consisting of 
# alphabetic characters and returns a string such that each word in the input 
# string is reversed while the order of the words in the input string is preserved. 
# The length of the input string must be equal to the length of the output string i.e. 
# there should be no extra trailing or leading spaces in your output string. 

# For example if:
# input_string = “this is a sample test”

# then the function should return a string such as:
# "siht si a elpmas tset"

# Preserve and Reserved function
def Preserve_and_Reserved(input_string):
    input_string = input_string.split()
    new_list = ''
    new_word = ''
    for word in input_string:
        for i in range(len(word)):
            new_word += word[-i-1]
        new_list += new_word
        if input_string.index(word) != len(input_string)-1:
            new_list += ' '
        new_word = ''
    return new_list

# Driver code tester
input_string = input("Please enter your string : ")
result = Preserve_and_Reserved(input_string)
print(result)

################### Sample Solution ###################
def _preserve_and_reverse_sample_(string):
    splitted_list = string.split()
    for x in range(0, len(splitted_list)):
        splitted_list[x] = splitted_list[x][::-1]
    # Initialize an output string
    output_string = ""
    for x in range(0, len(splitted_list)):
        output_string += splitted_list[x] + " "
    # Strip any white spaces
    output_string = output_string.strip()
    return output_string