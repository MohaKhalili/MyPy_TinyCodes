# A function that accepts two lists A and B and returns a new list 
# which contains all the elements of list A followed by elements of 
# list B. Notice that the behaviour of this function is different 
# from list.extend() method because the list.extend() method extends 
# the list in place, but here you are asked to create a new list and 
# return it. Your function should not return the original lists. For 
# example if the input lists are:

# A = ['p', 'q', 6, 'k']
# B = [8, 10]

# Then your function should return a list such as:

# ['p', 'q', 6, 'k', 8, 10]

# method 1
def List_Extending1(my_list1, my_list2):
    output = []
    for i in range(len(my_list1)):
        output.append(my_list1[i])
    for i in range(len(my_list2)):
        output.append(my_list2[i])
    return output

# method 2
def List_Extending2(my_list1, my_list2):
    return my_list1 + my_list2

# getting list from input
def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = input("enter list element : ")
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list1 = list_create()
my_list2 = list_create()
result = List_Extending2(my_list1, my_list2)
print(result)