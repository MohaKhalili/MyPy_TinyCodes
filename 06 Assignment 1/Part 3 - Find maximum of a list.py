# a function which accepts an input list of numbers and returns the largest number in the list.

# Type your code here
def max_num(numbers):
    maXI = numbers[0]
    for i in numbers:
        if i > maXI:
            maXI = i
    return maXI