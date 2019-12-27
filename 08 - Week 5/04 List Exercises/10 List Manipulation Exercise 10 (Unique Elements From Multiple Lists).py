# A function that accepts two input lists and returns a new 
# list which contains only the unique elements from both lists.


def Unique_Elements_From_Multiple_Lists(my_list1, my_list2):
    one_list = my_list1 + my_list2
    output = []
    for i in range(len(one_list)):
        if one_list[i] not in output:
            output.append(one_list[i])
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
my_list1 = list_create()
my_list2 = list_create()
result = Unique_Elements_From_Multiple_Lists(my_list1, my_list2)
print(result)