# In this function the unique common elements in two
# separate lists are collected and put in a new list.

def unique_common(a, b):
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

# driver for test unique_common function
x = [5, 6, -7, 8, 8, 9, 9, 10]
y = [2, 4, 8, 8, 5, -7]
z = unique_common(x, y)
print(z)