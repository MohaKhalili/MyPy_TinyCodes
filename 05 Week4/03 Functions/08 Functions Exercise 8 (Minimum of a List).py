# a function which accepts an input list of numbers and returns the smallest 
# number in the list (Do not use python's built-in min() function).

# Type your code here
def min_num(numbers):
    miNN = numbers[0]
    for i in numbers:
        if i < miNN:
            miNN = i
    return miNN