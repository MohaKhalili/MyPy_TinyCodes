# a function that accepts a list of integers and returns the average. 
# Assume that the input list contains only numbers.

# Type your code here
def miangin(numbers):
    sum_num = 0
    counter = 0
    for i in numbers:
        sum_num = sum_num + i
        counter = counter + 1
    miangin = sum_num / counter
    return miangin