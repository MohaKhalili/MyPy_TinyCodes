# A function that accepts a list that contains positive integers 
# and returns a new list which contains all the elements from 
# original list but adds 1 to those elements which are odd. 
 

# For example if :
# input_list = [12, 3, 4, 5, 6]
# Then your function should return a list such as:
# [12, 4, 4, 6, 6]

# method 1
def Modifying_List1(my_list):
    output = []
    for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            output.append(my_list[i] + 1)
        else:
            output.append(my_list[i])
    return output

# method 2
def Modifying_List2(input_list):
    for i in range(len(input_list)):
        if input_list[i] % 2 != 0:
            input_list[i] = input_list[i] + 1
    return input_list
  
# getting list from input
def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of list elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input("enter the list element : "))
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list = list_create()
result = Modifying_List1(my_list)
print(result)