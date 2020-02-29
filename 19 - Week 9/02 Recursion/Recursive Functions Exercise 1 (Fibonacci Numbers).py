# A function named nested_list_sum that receives a nested list of integers 
# as parameter and calculates and returns the total sum of the integers in 
# the list using recursion. Keep in mind that the inner elements may be 
# integers or other nested lists themselves.

# For example, when your function is called as:
# nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]])
# Then, your function should return the total sum as
# 10

################### My Solution ###################
def calculate_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

################### Driver code ###################
number = int(input("Please enter your number for fibonacci series : "))
result = calculate_fibonacci(number)
print(result)