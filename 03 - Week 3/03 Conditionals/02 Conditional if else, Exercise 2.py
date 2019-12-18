# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

my_list = [ "cat", 2, "dog", 4]
if 2 in my_list:
    print('yes')
else:
    print('no')
###################################################################
my_list = [ "cat", 2, "dog", 4]
x = 5 in my_list
if x:
    print('yes')
else:
    print('no')
###################################################################
my_list = [ 'dog', 'cat', 'worm', 'cow']
if 'dog' not in my_list:
    print('true')
else:
    print('false')
###################################################################
my_list = [ 'dog', 'cat', 'worm', 'cow']
if 'car' in my_list:
    print('true')
else:
    print('false')
###################################################################
my_list = [ 'dog', 'cat', 'worm', 'cow']
if 'w' in my_list:
    print('true')
else:
    print('false')