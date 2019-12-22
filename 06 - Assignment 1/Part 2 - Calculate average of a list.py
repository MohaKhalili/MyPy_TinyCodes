# A function that accepts a list of integers and returns the average. 
# Assume that the input list contains only numbers.

# Type your code here
def my_average(numbers):
    sum_num = 0
    counter = 0
    for i in numbers:
        sum_num = sum_num + i
        counter = counter + 1
    my_average = sum_num / counter
    return my_average

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
result = my_average(my_list)
print("The average of list elements is : ",result)