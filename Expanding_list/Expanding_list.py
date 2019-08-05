# Extending a List Without List Functions
# a function that accepts two lists A and B and returns a new list which
# contains all the elements of list A followed by elements of list B. 

# getting the inputs
n = input("please enter list one: ")
m = input("please enter list two: ")

# the function that i written
def Expanding_list(list1, list2):
    MyList = list1 + list2
    return MyList

# driver test for this function
listTEST = Expanding_list(m,n)
print (listTEST)