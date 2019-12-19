# This part includes 10 tiny questions

# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

a = 14 // 3
b = 4 > 5
print( a and b)
###################################################################
x = False
y = 0 > 10
print(y or x)
###################################################################
x = ['cat', 2.5, 'dog']
y = 'cat' in x
print(y)
###################################################################
x = "python course"
print("cours" not in x )
###################################################################
my_list = [ 13, 'cat', 5.6, 'cow']
if 'dog' in my_list:
    print('bark')
else:
    print('meow')
###################################################################
my_list = [ 'dog', 'cat', 'worm', 2.3]
if 'doc' in my_list:
    my_list[1] = 4
else:
    my_list[2] = 6
print (my_list[1],my_list[2])
###################################################################
x = 10
if x > 5 :
    x = x + 5
if x < 12 :
    x = x + 5
if x == 15 :
    x = x + 5
print(x)
###################################################################
x = 20
if True :
    x = x + 10
if x == 20:
    x = x + 30
else:
    x = x + 40
print(x)
###################################################################
x = 4
if "z" in "computer science":
    x = x + 10
elif 5 % 3 == 2:
    x = x + 18
elif 5>4:
    x = x + 30
else:
    x = x + 5
print (x)
###################################################################
x = "c"
y = 3
if "x" in "computer science":
    y = y + 5
else:
    y = y + 10
if x in "computer science":
    y = y + 20
else:
    y = y + 40
print (y)