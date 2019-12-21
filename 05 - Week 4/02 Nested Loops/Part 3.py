# There is 3 tiny question

# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

m = 1
for x in [1,2,3]:
    for y in [3,1,4]:
        if x == y:
            m = m * x 
print (m)
###################################################################
m = 1
my_list_1 = [2 , 4, 1]
for x in my_list_1:
    for y in range(1,3):
        if (x + y) % 3:
            m = m * x
print (m)
###################################################################
m = 0
my_str_1 = "university"
my_str_2 = "mississipy"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 == char_2:
            m = m + 1
print(m)