def Decussate(MyList):
    MyNewList = []
    for i in range(0,len(MyList),2):
        MyNewList.append(MyList[i])
    return MyNewList

MyList = ["we", "love", "python", "so","much"]
e = Decussate(MyList)
print(e)
