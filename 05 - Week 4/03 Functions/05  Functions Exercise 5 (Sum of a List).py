# A function that accepts a list of integers and returns the sum of all the numbers in the list.
# Assume that the input list contains only numbers. Do NOT use the built-in sum() function.

# Type your code here
def Sum_of_List(numbers):
    sum_list = 0
    for i in numbers:
        sum_list = sum_list + i
    return sum_list

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
result = Sum_of_List(my_list)
print(result)