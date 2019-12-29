# a function which accepts an input string and returns a reverse of
# the input string while the case for every single character is
# reversed. The input string for this function would be a sentence
# (words separated by spaces) consisting of alphabetic characters.

def Reversed_and_Case_Swapped(input_string):
    new_string = ""
    for my_index in range(len(input_string)-1,-1,-1):
        if input_string[my_index].islower():
            new_string = new_string + input_string[my_index].upper()
        elif input_string[my_index].isupper():
            new_string = new_string + input_string[my_index].lower()
        elif input_string[my_index] == " ":
            new_string = new_string + " "
    return new_string

# driver code test
String = "Hello Python World"
result = Reversed_and_Case_Swapped(String)
print(result)