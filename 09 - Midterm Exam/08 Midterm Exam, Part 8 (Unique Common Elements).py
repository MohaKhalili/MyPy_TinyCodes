# A function named unique_common that accepts two lists both of which 
# contain integers as parameters and returns a sorted list (ascending 
# order) which contains unique common elements from both the lists. If 
# there are no common elements between the two lists, then your function 
# should return the keyword None.


# method 1
def unique_common1(a, b):
    output_list = []
    for i in range(len(a)):
        if (a[i] in b) and (a[i] not in output_list):
            output_list.append(a[i])
    output_list.sort()
    return output_list

# method 2
def unique_common2(a, b):
    MyList = []
    for i in a:
        for j in b: 
            if i == j:
                if i not in MyList:
                    MyList.append(i)
    MyList.sort()
    if MyList == []:
        return None
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
my_list1 = list_create()
my_list2 = list_create()
result = unique_common1(my_list1, my_list2)
print(result)

################### Instructor function ###################
def _unique_common_elements_sample_ed2_(a, b):
    common = []
    for items in a:
        if items in b:
            common.append(items)
    if not common:
        return None
    unique = []
    for items in common[:]:
        if items not in unique:
            unique.append(items)
    return sorted(unique)