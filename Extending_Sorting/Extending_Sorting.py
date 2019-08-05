# Extending and Sorting
# a function that accepts two lists both of which contain integers and returns a new 
# list which contains all the elements from both lists sorted in descending order. 

# top function is here for extending 
def Extending_Sorting(List1, List2):
    List1.extend(List2)

# And thus the subfunction for sorting is laughing to you here :) 
    def sorting_list(MyList):
        sorted_List = []
        i = 0
        while len(MyList) > 0 :
            max_num = MyList[0]
            for j in range(len(MyList)):
                if max_num < MyList[j]:
                    max_num = MyList[j]
            sorted_List.insert(i,max_num)
            MyList.pop(MyList.index(max_num))
            i = i + 1 
        return sorted_List

    result = sorting_list(List1)
    return result

# driver test for test
l1 = [3,4,5]
l2 = [6,4,2]
t = Extending_Sorting(l1,l2)
print (t)