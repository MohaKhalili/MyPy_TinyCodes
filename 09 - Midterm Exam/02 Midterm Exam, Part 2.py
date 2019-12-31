# What will be printed after each of the following code segments? 
# If error, then write Error

my_list = []
for k in range(1,101,20):
    my_list.append(k)
print (my_list[: :2] )
###################################################################
def my_fun(x):
    for k in range (len(x)):
        x.extend(x[:k])
m = [1,5,3]
my_fun(m)
print(m)
###################################################################
def my_fun(x):
    for k in range (len(x)):
        x.append(x[:k])
m = [1,5,3]
my_fun(m)
print(m)
###################################################################
my_list = [9, 8, 7]
for k in range (3):
    my_list.insert(-k, k+1)
print(my_list)
###################################################################
my_list = [12, "cat", 3.4, "dog", 62]
new_list = []
for k in range(5):
    if k % 2:
        m = my_list.pop(k)
        new_list.append(m)
print(new_list)
###################################################################
def my_fun(my_list,s,e):
    del (my_list[s:e])
 
values = [2, 9, 16, 3, 24, 13, 15]
my_fun(values,-6,-4)
my_fun(values,2,4)
print(values)
###################################################################
def my_fun(i):
    values = []
    values.append(i)
    return values
my_fun(5)
print(my_fun(3))
###################################################################
def my_fun(m):
    x = []
    for k in range(len(m)):
        if m[k] % 3 == 0 and m[k] % 2:
            x.insert(k, m[k])
    return x
 
values = [2, 9, 16, 3, 24, 13, 15]
print(my_fun(values))
###################################################################
def my_fun(m, increment):
    x = 0
    while x < len(m):
        m[x] = m[x] + increment
        x = x + 1
    return m 

values = [4, 3, 7]
print(my_fun(values, 2))
###################################################################
def my_fun(m):
    x = m[:]
    for k in x:
        if type(k) == int:
            m.remove(k)

values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
my_fun(values)
print(values)