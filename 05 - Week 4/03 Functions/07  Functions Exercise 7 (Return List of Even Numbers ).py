# A function which accepts an input list of numbers and returns a list which includes only 
# the even numbers in the input list. If there are no even numbers in the input numbers then
# your function should return an empty list.

# Type your code here
def even_between(list_number):
    MyList = []
    for i in range(len(list_number)):
        if list_number[i] % 2 == 0:
            MyList.append(list_number[i])
    return MyList

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
result = even_between(my_list)
print(result)