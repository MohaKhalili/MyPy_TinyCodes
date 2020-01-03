# A function called pattern_sum that receives two single digit positive integers,
# (k and m) as parameters and calculates and returns the total sum as:
# k + kk + kkk + .... (the last number in the sequence should have m digits)

# method 1
def pattern_sum1(a, b):
    a = str(a)
    sum_num = 0
    for i in range(1, b+1):
        sum_num += int(a*i)
    return sum_num

# method 2
def pattern_sum2(a, b):
    MyList = []
    a = str(a)
    for i in range(1,b+1):
        ST = i*a
        MyList.append(ST)
        MyList[i-1] = int(MyList[i-1])
        print(MyList)
    sum_MyList = 0
    for j in range(len(MyList)):
        sum_MyList = sum_MyList + MyList[j]
    return sum_MyList

number = int(input("Please enter your number : "))
iter = int(input("Please enter desired iteration : "))
result = pattern_sum1(number, iter)
print(result)

################### Instructor function ###################
def _chain_of_number_sample_ed2_(a, b):
    chain_list = []
    my_sum = 0
    for x in range(1, b+1):
        chain_list.append(x*str(a))
    for items in chain_list:
        my_sum = my_sum + int(items)

    return my_sum