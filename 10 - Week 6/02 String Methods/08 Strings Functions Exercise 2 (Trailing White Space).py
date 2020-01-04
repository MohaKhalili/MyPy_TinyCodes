# A function that accepts an input string consisting of alphabetic 
# characters and removes all the trailing whitespace of the string 
# and returns it without using any .strip() method. For example if:
# input_string = "  Hello       "
# then your function should return an output string such as:
# output_string = "  Hello"

# method 1
def Trailing_White_Space1(my_str):
    len_str = len(my_str)
    new_str = ''
    for i in range(len(my_str)):
        if my_str[i-1] != " " and my_str[i] == " " and my_str[i+1] == " ":
            break
        else:
            new_str += my_str[i]
    return new_str

# method 2
def Trailing_White_Space2(str):
    index = []
    for i in range(len(str)-1,0,-1):
        if str[i] != " ":
            index = i + 1
            break
    str_new = str[:index]
    return str_new

my_str = input("Please enter your string : ")
result = Trailing_White_Space2(my_str)
print(result)

 
################### Sample Solution ###################
def _remove_trailing_whitespace_sample_(string):
    my_index = None
    i = len(string)
    while i > 0:
        if string[i-1] != " ":
            my_index = i
            break
        i = i - 1
    # slice the string from 0 to that index
    new_string = string[:my_index]
    return new_string