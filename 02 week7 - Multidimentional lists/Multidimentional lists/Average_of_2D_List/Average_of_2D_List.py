# a function that accepts a 2 Dimensional list of integers and returns the average.
def Average_of_2D_List(my_list):
    total = 0
    count = 0
    for dim1 in my_list:
        for index in range(len(dim1)):
            total = total + dim1[index]
            count = count + 1
    average = total / count
    return average

# driver code tester
my_list = [[2, 3],[6, 9]]
result = Average_of_2D_List(my_list)
print(result)