# You are trying to divide two numbers and you need to write a function to perform the task. 
# The function takes two arguments. The first argument is a float but you are unsure about 
# the second argument (there is a chance that the second argument could be a zero). Write a 
# function that takes a float and an unknown input and tries to handle the error when you 
# try to divide the float by the unknown input using the try..except..else clause. 
# The unknown input could be either an integer or a string or a float. If the operation fails 
# your function should return the value None (exactly without the quotes), If successful your 
# function should return the result.

################### My Solution ###################
def func_divide(float_num, unknown_input):
    try:
        output = float_num / unknown_input
    except:
        return None
    else:
        return output

################### Sample Solution ###################
def _handle_division_error_(my_float, unknown):
    try:
        result = my_float / unknown
    except (ZeroDivisionError, TypeError):
        return None
    else:
        return result

################### Driver Code ###################
float_num = float(input('Please give me float input : '))
my_string = input('Please give me string input : ')
result = func_divide(float_num, my_string)
print(result)