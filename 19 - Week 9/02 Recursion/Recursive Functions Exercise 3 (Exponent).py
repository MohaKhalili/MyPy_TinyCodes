# A function named calculate_exponent that receives two positive integers a and 
# b as parameter and calculates and returns a to the power of b using recursion. 
# For example, when your function is called as:
# calculate_exponent(5, 3)
# Then, your function should return:
# 125

################### My Solution ###################
def calculate_exponent(a, b):
    if b == 0:
        return 1
    else:
        return a * calculate_exponent(a,b-1)

################### Driver Code ###################
number_a = int(input("Please enter your number_a for exponent calculation : "))
number_b = int(input("Please enter your number_b for exponent calculation : "))
result = calculate_exponent(number_a, number_b)
print(result)