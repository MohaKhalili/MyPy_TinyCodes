# a function that accepts a string of words separated by spaces
# consisting of alphabetic characters and returns a string such
# that each word in the input string is reversed while the order
# of the words in the input string is preserved. The length of
# the input string must be equal to the length of the output
# string i.e. there should be no extra trailing or leading
# spaces in your output string.

def Preserve_and_Reverse(input_string):
    input_string = input_string.split()
    new_string = ""
    for word in input_string:
        for my_index in range(len(word) - 1, -1, -1):
            new_string = new_string + word[my_index]
        if input_string.index(word) != (len(input_string)-1):
            new_string = new_string + " "
    return new_string

# driver code test
String = "this is a sample test"
result = Preserve_and_Reverse(String)
print(result)