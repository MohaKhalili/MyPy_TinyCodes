# a function that accepts two positive integers as function parameters and returns their least 
# common multiple (LCM). The LCM of two integers a and b is the smallest (non zero) positive 
# integer that is divisible by both a and b. For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10.

# Remember that you are not asked to print anything. So, your function should return the LCM and not print it. 
# You do not need to call your function, it will automatically be called and tested for correctness with the 
# test cases we provide. You only need to write one function and we will test your program with the first 
# function that appears in your code. So, if you want to write more than one function to help you solve the 
# problem, remember to embed the helper functions inside the first function. 

# method 1 with GCD
def LCM(a,b):
    def GCD(a,b):
        if a == 0: 
            return b 
        return GCD(b % a, a)
    result = (a*b) / GCD(a,b)
    return result

# method 2
def LCM2(number1, number2):
    min_number = min(number1, number2)
    for LCM in range(min_number,(number1*number2)+1):
        if (LCM % number1 == 0) and (LCM % number2 == 0):
            return LCM

# Driver code test
n1 = int(input("Please enter your first number : "))
n2 = int(input("Please enter your second number : "))
result = LCM(n1, n2)
print("least common multiple of ",n1,"and",n2,"is",result)

################### Instructor function ###################
# def _least_common_multiple_sample_(a, b):
#     # first make a backup/copy of a
#     copy_of_a = a
#     # While the remainder when a is divided by b is not 0
#     # continue to add a to its backup (copy_of_a)
#     while (copy_of_a % b) != 0:
#         copy_of_a = copy_of_a + a
#     return copy_of_a