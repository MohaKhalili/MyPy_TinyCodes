# Counting an item in a list
# a function that accepts a list and a value of an element and returns
# the count of how many times that element appears in the list

def Counting_item(MyList, param):
    i = 0
    for j in range(len(MyList)):
        if MyList[j] == param:
            i = i + 1
    return i

# driver test for this funtion
l = [3,5,7,9,3,45,3,7,54,2,4,3,2,1,2,3,3,4,5,6,76,7,3]
param = 3
e = Counting_item(l, param)
print(e)