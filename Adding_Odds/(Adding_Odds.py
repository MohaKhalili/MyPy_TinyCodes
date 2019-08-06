# Adding Odds from 2 Lists
# a function that accepts two lists both of which consists of integers 
# and returns the total sum of all the odd integers from both lists.
def Adding_Odds(List1, List2):
    MyList = []
    for i in range(len(List1)):
        if List1[i] % 2 != 0:
            MyList.append(List1[i])
    for i in range(len(List2)):
        if List2[i] % 2 != 0:
            MyList.append(List2[i])
    sum_List = 0
    for i in range(len(MyList)):
        sum_List = sum_List + MyList[i]
    return sum_List

# driver test code for the function
l1 = [3,4,5,6,78,2,3,534,2,3,4,5]
l2 = [3,4,2,3,4,9]
result = Adding_Odds(l1,l2) 
print(result)