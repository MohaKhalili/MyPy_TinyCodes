def items_price(List1, List2):
    if len(List1) == len(List2):
        ALLprice = 0
        for i in range(len(List1)):
            ALLprice = ALLprice + (List1[i]*List2[i]) 
        return ALLprice
    else:
        return None

a = [2, 3, 5, 7, 9]
b = [5, 8, 4, 1, 11]
x = items_price(a,b)
print(x)