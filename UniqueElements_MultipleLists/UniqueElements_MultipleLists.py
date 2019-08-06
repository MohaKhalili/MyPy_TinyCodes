# Unique Elements From Multiple Lists
# a function that accepts two input lists and returns a new list 
# which contains only the unique elements from both lists.

def UniqueElements_MultipleLists(List1, List2):
    List1.extend(List2)
    new_List = []
    for i in range(0,len(List1)):
        if List1[i] not in new_List:
            new_List.append(List1[i])
    return new_List

l1 = [1,1,2,3,5,6,6,7,8,9,9]
l2 = [3,4,7,4,5]
result = UniqueElements_MultipleLists(l1, l2)
print(result)