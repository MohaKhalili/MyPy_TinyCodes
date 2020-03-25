# You are trying to concatenate two strings and you need to write a function 
# to perform the task. The function takes two arguments. You do not know the 
# type of the first argument in advance but the second argument is certainly 
# a string. Write a function that takes an unknown input and a string as input 
# and tries to handle the error when you try to concatenate this unknown input 
# to the string using the try..except..else clause. The unknown input could be 
# either an integer or a string or a float. If the concatenation fails your 
# function should return the value None (exactly without the quotes), 
# If successful your function should return the resulting string.

################### My Solution ###################
def func_comb(unknown_input, string):
    try:
        output = unknown_input + string
    except:
        return None
    else:
        return output

################### Sample Solution ###################
def _handle_concatenation_error_sample_(unknown, string):
    try:
        result = unknown + string
    except TypeError:
        return None
    else:
        return result

################### Driver Code ###################
unknown = int(input('Please give me integer input : '))
my_string = input('Please give me string input : ')
result = func_comb(unknown, my_string)
print(result)