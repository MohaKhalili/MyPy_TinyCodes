# What will be printed after each of the following code segments? 
# If error, then write Error.

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

count = 20
for x in range(0,10):
    count = count - 1
    if x == 2:
        break
print(count)
###################################################################
k = 1
while k<5:
    if k % 7 == 0:
        break
    k = k + 2
print(k)
###################################################################
my_list = ["dog", 24, "cat", 12]
count = 0
for element in my_list:
    if element == "cat":
        continue
    count = count + 1
print(count)