# A function that receives a positive integer as function parameter and returns True 
# if the integer is a perfect number, False otherwise. A perfect number is a number 
# whose sum of the all the divisors (excluding itself) is equal to itself. 

# For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6.
# Therefore, 6 is a perfect number.

# Remember, that you are not asked to print anything. So, your function should return either True or False. 
# You do not need to call your function, it will automatically be called and tested for correctness with the
# test cases we provide. You only need to write one function and we will test your program with the first function
# that appears in your code. So, if you want to write more than one function to help you solve the problem, remember 
# to embed the helper functions inside the first function. 

# method 1
def is_complete(n):
    is_complete = False
    sum_n = 0
    for counter in range(1,n):
        if n % counter == 0:
            sum_n = sum_n + counter
    if sum_n == n:
        is_complete = True
    return is_complete

# method 2
def completed_number(number):
    sum_divisors = 0
    for divisor in range(1,n):
        # Check for the remainder when n is divided by number
        # if the remainder is 0 that means number is a divisor of n
        if number % divisor == 0:
            sum_divisors = sum_divisors + divisor
    # check if the sum of the divisors equals to n itself
    if sum_divisors == number:
        return True
    else:
        return False

# Driver code test
n = int(input("Please enter your number : "))
result = completed_number(n)
print("complete number status : ",result)