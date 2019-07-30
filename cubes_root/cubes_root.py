def cubes_root(k):
    MyList = []
    for i in range(1,k):
        MyList.append(i ** (1/3))
    return MyList

e = cubes_root(10)
print(e)
