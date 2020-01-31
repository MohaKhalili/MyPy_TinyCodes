# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match 
# the correct Python output.

my_list = [[3,4],[6,7],[10,12]]
print(my_list[0:2])
#################################################################
my_list = [[3,5,6], [6,4,2], [9,4,8]]
for k in range (len(my_list)):
    my_list[k][0] = 1
print(my_list)
#################################################################
my_list = [[6,2],[3,9,5]]
x = 0
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        x = x + my_list[m][k] 
print(x)
#################################################################
my_list = []
for m in range(0,2):
    new_list = []
    for k in range(4,6):
        new_list.append(k)
    my_list.append(new_list)
print(my_list)
#################################################################
my_list = [[3,5],[2,9],[4,7]]
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        my_list[m][k] = my_list[m][k] * 2
print(my_list)
#################################################################
numbers={1: "uno", 3:"two", "tres":3}
print(numbers.pop(3))
#################################################################
numbers={"one": [1,"uno"], "two": [2,"dos"]}
print (numbers["two"][1][2])
#################################################################
# d={1:"one", "two": 2 , 3: "tres"}
# print (d[2])
#################################################################
d={1:"one", "two": 2 , 3: "tres"}
print (d.get(2))
#################################################################
# numbers = {["one","two"]: 1, "two": 2}
# print(numbers)