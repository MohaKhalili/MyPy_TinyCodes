# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

my_list = [[2,3],[6,5],[10,9]]
print(my_list[0:2])
#####################################################################
my_list = []
for m in range(0,2):
    new_list = []
    for k in range(2,4):
        new_list.append(k)
    my_list.append(new_list)
print(my_list)
#####################################################################
my_list = []
for k in range(1,101,10):
    my_list.append(k)
print (my_list[: :3] )
#####################################################################
my_list = [2, 3, 4]
for k in range (3):
    my_list.insert(-k, k+1)
print(my_list)
#####################################################################
def my_fun(x):
    for k in range (len(x)):
        x.extend(x[:k])
m = [2,4,3]
my_fun(m)
print(m)
#####################################################################
def my_fun(a):
    a[0] = 'new name'     
    a[1] = 'john'      

x = ['old name', 'jack']
my_fun(x)
print (x)
#####################################################################
my_list = [[3,2],[2,6,4]]
x = 0
new_list=[]
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        x =  my_list[m][k]
        new_list.append(x)
        
print(new_list)
#####################################################################
m = 0
my_str_1 = "car"
my_str_2 = "cat"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 != char_2:
            m = m + 1
print([m])
#####################################################################
x = "bye bob"
print ([x.strip("b")])
#####################################################################
m = 0
for x in range (4,6):
   for y in range (2,4):
      m = m + x + y
print ([m])