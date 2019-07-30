#Check a list to see if it has front and back symmetry

def crazy_list(MyList):
    Condition = True
    for i in range(len(MyList)):
        if MyList[i] != MyList[-i-1]:
            Condition = False 
    
    return Condition

listnew = [4, 5, 6, 7, 8, 4, 5, 2]
x = crazy_list(listnew)
print(x)