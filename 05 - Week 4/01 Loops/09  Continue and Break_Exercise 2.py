# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

my_str = "university"
count = 0
for char in my_str:
    if char == "i":
        continue
    else:
        count = count + 1
print(count)
###################################################################
my_str = "university"
count = 0
for char in my_str:
    count = count + 1
    if char == "e":
        break  
print(count)
###################################################################
my_list = [6, 5, 7, 2, 3, 5, 7, 8] 
count = 0
for number in my_list:
    if number == 5 or number == 7:
        continue
    else:
        count = count + number
print(count)