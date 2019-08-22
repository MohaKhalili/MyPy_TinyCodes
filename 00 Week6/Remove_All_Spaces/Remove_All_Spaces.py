# a function which accepts an input string consisting
# of alphabetic characters and spaces and returns the
# string with all the spaces removed.

def Remove_All_Spaces(my_str):
    new_str = ""
    for i in range(len(my_str)):
        if ord(my_str[i]) != 32:
            new_str = new_str + chr(ord(my_str[i]))
    return new_str

# driver code
String = "hell there"
result = Remove_All_Spaces(String)
print(result)