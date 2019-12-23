# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match 
# the correct Python output.

count = 0
for x in range(2,5):
    count = count + x
print(count)
##################################################################
k = 10
while k > 2:
    x = k / 2
    k = k - 1
print(x)

##################################################################
count = 10
for x in range(0,7):
    count = count + 2
    if x == 4:
        break
print(count)

##################################################################
k = 1
count = 0
while count < 10:
    if k % 4 == 0:
        break
    count = count + k
    k = k + 1
print(count)

##################################################################
my_list = ["pet" ,"dog", 35, "cat", 23]
count = 0
for item in my_list:
    if type(item) == str:
        continue
    count = count + 1
print(count)

##################################################################
m = 0
my_str= "mississipi"
for char in my_str:
    if char == "s":
        continue
    if char == "p":
        break
    m = m +1
print(m)

##################################################################
m = 0
for x in range (4,6):
   for y in range (2,4):
      m = m + x + y
print (m)

##################################################################
m = 0
x = 1
while x < 5:
    y = 1
    while y < 4:
        m = m + y
        y = y + 3
    x = x + 2
print(m)

##################################################################
m = 0
my_list_1 = [1, 2, 5]
my_list_2 = [1, 3, 2, 6, 5]
for x in my_list_1:
    for y in my_list_2:
        if x == y :
            m = m + 1
print (m)

##################################################################
m = 0
my_str_1 = "cat"
my_str_2 = "pet"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 != char_2:
            m = m + 2
print(m)