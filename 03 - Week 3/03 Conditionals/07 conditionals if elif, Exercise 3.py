# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

x = 100
if x > 10 :
    x = x + 10
if x > 20 :
    x = x + 50
print(x)
###################################################################
x = 100
if x > 10 :
    x = x + 10
elif x > 20 :
    x = x + 50
else:
    x = x + 70
print(x)