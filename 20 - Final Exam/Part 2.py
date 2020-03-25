# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

x = "mississipi"
print (x.replace('i','z',2))
###################################################################
x = ["duck", "car", "pet"]
print ("AA".join(x))
###################################################################
k = 10
while k > 2:
    x = k / 3
    k = k - 1
print(x)
###################################################################
numbers={"one": [1,"uno"], "two": [2,"dos"]}
print (numbers["one"][1][2])
###################################################################
# d={1:"one", "two": 2 , 3: "tres"}
# print (d["tres"])
###################################################################
my_string = "x = {0:#^7d} and y = {1:@>8.3f}".format(5, 0.3)
print (my_string)
###################################################################
print('A{0:B^9}C'.format('dog'))
###################################################################
def my_fun(x):
    z = 0
    for item in x:
        m = x.count(item)
        if m > z:
            z = m
    return z

y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
print (my_fun(y))
###################################################################
list_1 = ["cat", 3, "cat" , 25, 12]
list_2 = ["car", 25, "dog" , 43]
count = 0
for item in list_1:
    if item in list_2:
        count = count + 1
print (count)
###################################################################
print('{0:,}'.format(12345678))