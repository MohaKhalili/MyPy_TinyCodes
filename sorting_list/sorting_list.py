# Sorting a List
# a function that accepts a list of integers and returns a 
# new list which is the sorted version (ascending order) of
# the original list (Original list should not be modified).

def sorting_list(MyList):
    sorted_List = []
    i = 0
    print(len(MyList))
    while len(MyList) > 0 :
        min_num = MyList[0]
        for j in range(len(MyList)):
            if min_num > MyList[j]:
                min_num = MyList[j]
        sorted_List.insert(i,min_num)
        MyList.pop(MyList.index(min_num))
        i = i + 1 
    return sorted_List

# driver test for this fuunction
x = [1,-3,10,0,-0.5]
y = sorting_list(x)
print(y)
