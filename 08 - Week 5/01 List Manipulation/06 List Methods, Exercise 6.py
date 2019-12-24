# What will be printed after each of the following code segments? 
# If error, then write Error

my_list = []
for x in range(2,11,3):
    my_list.append(x)
print(my_list)
  
#################################################################
my_list = []
for x in range(4,30,3):
    my_list.append(x)
print(my_list)
  
#################################################################
a = range(3,20,4)
b = []
for k in a:
    if k % 2:
        b.append(k)
print (b)

#################################################################
my_list = []
for x in range(1,10):
    if not (x % 3):
        my_list.append(x)
print(my_list)