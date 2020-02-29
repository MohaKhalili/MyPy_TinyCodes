# A function named nested_list_sum that receives a nested list of integers 
# as parameter and calculates and returns the total sum of the integers in 
# the list using recursion. Keep in mind that the inner elements may be 
# integers or other nested lists themselves.

# For example, when your function is called as:
# nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]])
# Then, your function should return the total sum as
# 10

################### My Solution ###################
def nested_list_sum(n):
    total = 0
    for element in n:
        if (type(element) == type([])):
            total = total + nested_list_sum(element)
        else:
            total = total + element
    return total

################### Driver Code ###################
my_list = [1, -1, [2, -2], [3, -3, [4, -4], 10]]
result = nested_list_sum(my_list)
print ("Sum is:", result)