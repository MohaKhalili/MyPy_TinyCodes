def odd_between(a,b):
    MyList = []
    if a<b:
        for i in range(a,b+1):
            if i % 2 == 1:
                MyList.append(i)
        MyList.reverse()
        return MyList
    else:
        return None

e = odd_between(9,11)
print(e)