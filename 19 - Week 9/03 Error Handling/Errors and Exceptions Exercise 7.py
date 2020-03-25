# You are trying to modify the content of a list and you need to write a function 
# to perform the task. The function takes three arguments. The first argument is 
# the list itself, the second argument is an index 'n' and the third argument is 
# a string. Your job is to set the 'n'th (index) item of the list as the given 
# string and return the modified list if successful. In case of a failure your 
# function should return the original list. Write a function that performs this 
# task using the try...except...else statements.

################### My Solution ###################
def list_modify(my_list, n, my_string):
    try:
        my_list.pop(n)
        my_list.insert(n,my_string)
    except:
        return my_list
    else:
        return my_list

################### Sample Solution ###################
def _handle_index_error_(my_list, index, string):
    try:
        my_list[index] = string
    except (IndexError, TypeError):
        return my_list
    else:
        return my_list

################### Driver Code ###################
my_list = [12,'salam',4.3]
n = 10
my_string = 'bye'
result = list_modify(my_list, n, my_string)
print(result)