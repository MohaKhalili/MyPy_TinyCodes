# a function which accepts an input string and returns a string where
# the case of the characters are changed, i.e. all the uppercase
# characters are changed to lower case and all the lower case
# characters are changed to upper case. The non-alphabetic
# characters should not be changed.
def Changing_Cases(my_str):
    new_str = ""
    for i in range(len(my_str)):
        if ord(my_str[i]) in range(65,91):
            new_str = new_str + chr(ord(my_str[i])+32)
        elif ord(my_str[i]) in range(97,123):
            new_str = new_str + chr(ord(my_str[i])-32)
        else:
            new_str = new_str + my_str[i]
    return new_str

# driver code for this function
String1 = "hello, I AM A code that Contain 3 kinds of data type"
result = Changing_Cases(String1)
print(result)