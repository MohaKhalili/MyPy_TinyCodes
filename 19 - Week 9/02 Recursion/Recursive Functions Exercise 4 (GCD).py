# A function named calculate_gcd that receives two positive integers a and b 
# as parameter and returns their greatest common divisor (GCD) using recursion.

# For example, when your function is called as:
# calculate_gcd(10, 15)
# Your function should return:
# 5

################### My Solution ###################
def calculate_gcd(a, b):
    if b==0: 
        return a
    else: 
        return calculate_gcd(b,a%b)

################### Driver Code ###################
number_a = int(input("Please enter your number_a for exponent calculation : "))
number_b = int(input("Please enter your number_b for exponent calculation : "))
result = calculate_gcd(number_a, number_b)
print ("The gcd of", number_a, "and", number_b, "is : ",result)