# A function which accepts an input string and returns a reverse of the 
# input string while the case for every single character is reversed. 

# The input string for this function would be a sentence (words separated
# by spaces) consisting of alphabetic characters. For example if:

# input_string = "Hello Python World"
# then the function should return a string such as:
# "DLROw NOHTYp OLLEh"

# Type your code here
def Reversed_and_Case_Swapped(input_string):
    input_string = input_string.swapcase().split()
    new_list = ''
    new_word = ''
    for j in range(len(input_string)):
        word = input_string[-j-1]
        for i in range(len(word)):
            new_word += word[-i-1]
        new_list += new_word
        if j != len(input_string)-1:
            new_list += ' '
        new_word = ''
    return new_list

# Driver code tester
input_string = input("Please enter your string : ")
result = Reversed_and_Case_Swapped(input_string)
print(result)

################### Sample Solution ###################
def _reverse_string_sample_(sample_string):
    output = ""
    i = -1
    # iterate the list from end to the front
    while i != (- (len(sample_string) + 1)):
        output = output + sample_string[i].swapcase()
        i = i - 1
    return output