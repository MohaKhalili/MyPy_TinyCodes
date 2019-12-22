# A function which accepts an input list of numbers and returns the 
# largest number in the list.

# Type your code here
def max_num(numbers):
    maXI = numbers[0]
    for i in numbers:
        if i > maXI:
            maXI = i
    return maXI

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
result = max_num(my_list)
print("The maximum of list elements is : ",result)