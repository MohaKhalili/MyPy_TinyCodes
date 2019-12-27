# A function that accepts a list and a value of an element and returns 
# the count of how many times that element appears in the list. 
# The behaviour of this function should be exactly like the 
# list.count() method. You may NOT use any built in list methods for this problem.

# counter function
def Counting_list(mylist, mystr):
    counter = 0
    for i in range(len(mylist)):
        if mylist[i] == mystr:
            counter = counter + 1
    return counter

# getting list from input
def list_create():
    lst = [] 
    # number of elemetns as input 
    n = int(input("Enter number of list elements : ")) 
  
    # iterating till the range 
    for i in range(0, n): 
        ele = input("enter the list element : ")
  
        lst.append(ele) # adding the element
    return lst 

# Driver code test
my_list = list_create()
my_string = input("Please enter the string : ")
result = Counting_list(my_list, my_string)
print(result)