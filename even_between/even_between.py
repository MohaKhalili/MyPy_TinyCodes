def even_between(a,b):
    MyList = []
    for i in range(a,b):
        if i % 2 == 0:
            MyList.append(i)
    return MyList

e = even_between(4,73)
print(e)