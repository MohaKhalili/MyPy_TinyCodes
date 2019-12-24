# A function that accepts a positive integer k and returns a list that 
# contains the first five multiples of k. The multiples should be calculated
#  starting from 1 to 5 (including both 1 and 5). For example the first five
#  multiples of 3 are 3, 6, 9, 12, and 15 

# method 1
def Multiples_List(k):
    MyList = []
    for i in range(1,6):
        MyList.append(k*i)
    return MyList

# method 2
def List_Multiples(number):
    counter = 1
    list = []
    multiple = number
    while (counter <= 5):
        if multiple % number == 0:
            list.append(multiple)
            multiple = multiple + number
        counter = counter + 1
    return list

# Driver code test
number = int(input("Please enter the number : "))
result = List_Multiples(number)
print(result)