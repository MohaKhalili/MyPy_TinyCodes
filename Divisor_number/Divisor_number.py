def Divisor_number(k):
    MyList = []
    for i in range(1,k+1):
        if k % i == 0:
            MyList.append(i)
    return MyList

e = Divisor_number(32)
print(e)