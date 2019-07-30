def Multiples_List(k):
    MyList = []
    for i in range(1,6):
        MyList.append(k*i)
    return MyList

e = Multiples_List(4)
print (e)