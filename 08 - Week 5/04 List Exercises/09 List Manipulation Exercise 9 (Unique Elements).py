# A function that accepts an input list and returns a new list which 
# contains only the unique elements(Elements should only appear one 
# time in the list and the order of the elements must be preserved 
# as the original list. ). 

def Unique_Elements(my_list):
    output = []
    for i in range(len(my_list)):
        if my_list[i] not in output:
            output.append(my_list[i])
    return output

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
result = Unique_Elements(my_list)
print(result)