# Unique Elements
# a function that accepts an input list and returns a new list which 
# contains only the unique elements(Elements should only appear one 
# time in the list and the order of the elements must be preserved 
# as the original list. ). 

def Unique_Elements(MyList):
    new_List = []
    for i in range(0,len(MyList)):
        if MyList[i] not in new_List:
            new_List.append(MyList[i])
    return new_List

# driver test code
l = [1,1,2,3,4,4,3,2,4,5,6,6,7,8,9,9]
result = Unique_Elements(l)
print(result)