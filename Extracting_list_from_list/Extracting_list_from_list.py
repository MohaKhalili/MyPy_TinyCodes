# Extracting a list from a list
# a function that accepts a list and return a new list which 
# contains all but the first and last elements of the original list.

def Extracting_list_from_list(MyList):
    MyList.pop(0)
    MyList.pop()
    return MyList

# drive test code for this funcking function :|
l = [3,4,5,6,3,45,3]
e = Extracting_list_from_list(l)
print(e)