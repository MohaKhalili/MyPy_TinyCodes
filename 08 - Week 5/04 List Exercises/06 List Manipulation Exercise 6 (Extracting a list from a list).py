# A function that accepts a list and return a new list which contains 
# all but the first and last elements of the original list.

# method 1
def Extracting_list_from_list(MyList):
    MyList.pop(0)
    MyList.pop()
    return MyList

# method 2
def Extracting_list_from_list(my_list):
    output = []
    for i in range(1, len(my_list)-1):
        output.append(my_list[i])
    return output

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
result = Extracting_list_from_list(my_list)
print(result)

################### Sample Solution ###################
# def _list_manipulation_sample4_(input_list):
#     newlist = input_list[1:-1]
#     return newlist