# a function that accepts two positive integers as function parameters and returns their least 
# common multiple (LCM). The LCM of two integers a and b is the smallest (non zero) positive 
# integer that is divisible by both a and b. For example, the LCM of 4 and 6 is 12, the LCM of 10 and 5 is 10.

# Remember that you are not asked to print anything. So, your function should return the LCM and not print it. 
# You do not need to call your function, it will automatically be called and tested for correctness with the 
# test cases we provide. You only need to write one function and we will test your program with the first 
# function that appears in your code. So, if you want to write more than one function to help you solve the 
# problem, remember to embed the helper functions inside the first function. 

# Type your code here
def LCM(a,b):
    def GCD(a,b):
        if a == 0: 
            return b 
        return GCD(b % a, a)
    result = (a*b) / GCD(a,b)
    return result