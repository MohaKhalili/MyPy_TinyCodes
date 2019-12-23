# a function that accepts a list of integers as parameter. Your function should return 
# the sum of all the odd numbers in the list. If there are no odd numbers in the list, 
# your function should return 0 as the sum.

# Remember that you are not asked to print anything. So, your function should just return
# the sum of all the odd numbers in the list. You do not need to call your function, it will
# automatically be called and tested for correctness with the test cases we provide. You only
# need to write one function and we will test your program with the first function that appears
# in your code. So, if you want to write more than one function to help you solve the problem, 
# remember to embed the helper functions inside the first function. 

# method 1
def odd_number(n):
    sum_n = 0
    for i in n:
        if i % 2 != 0:
            sum_n = sum_n + i
    return sum_n

# method 2
def sum_odd_number(list):
    sum_number = 0
    for i in range(len(list)):
        if list[i] % 2 == 1:
            sum_number = sum_number + list[i]
    return sum_number 

def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter list element : ")) 
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list = list_create()
result = sum_odd_number(my_list)
print(result)

################### Sample Solution ###################
# def _sum_of_odds_sampleX_(my_list):
#     my_sum = 0
#     for items in my_list:
#         if items % 2 != 0:
#             my_sum = my_sum + items
#     return my_sum