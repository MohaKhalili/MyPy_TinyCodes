# a function which accepts an input list of numbers and returns the smallest 
# number in the list (Do not use python's built-in min() function).

# Type your code here
def min_num(numbers):
    miNN = numbers[0]
    for i in numbers:
        if i < miNN:
            miNN = i
    return miNN

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
result = min_num(my_list)
print(result)