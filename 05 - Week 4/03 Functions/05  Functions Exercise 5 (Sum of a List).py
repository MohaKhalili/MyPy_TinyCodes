# a function that accepts a list of integers and returns the sum of all the numbers in the list.
# Assume that the input list contains only numbers. Do NOT use the built-in sum() function.

# Type your code here
def my_list(numbers):
    sum_list = 0
    for i in numbers:
        sum_list = sum_list + i
    return sum_list
