# A special pattern for making a NumList and 
# and adding elements of a that.

# Imagine two numbers a and b that make a list of 
# patterns with [a, aa, aaa, ..., a(b)], the goal 
# is to first create this pattern by taking two 
# numbers from the input And then adding the 
# elements of that list.

def pattern_sum(a, b):
    MyList = []
    a = str(a)
    for i in range(1,b+1):
        ST = i*a
        MyList.append(ST)
        MyList[i-1] = int(MyList[i-1])
    sum_MyList = 0
    for j in range(len(MyList)):
        sum_MyList = sum_MyList + MyList[j]
    return sum_MyList

# Driver for this function
x = pattern_sum(4,5)
print(x)
