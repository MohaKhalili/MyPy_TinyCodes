# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the
# correct Python output.

x = 0
if 5 in [1, 2, 3, 4]:
    x = x + 1
elif 4 == 2:
    x = x + 2
elif 7 > 4:
    x = x + 3
else:
    x = x + 4
print (x)
###################################################################
x = 5
if 8 % 4:
    x = x - 1
elif 3 < 4 / 2:
    x = x - 2
elif "t":
    x = x - 3
else:
    x = x - 4
print (x)
###################################################################
x = 12
if "x" in "meow" and 4 > 2+1 :
    x = x / 2
elif 6 % 2 != 0 :
    x = x / 3
elif 2 in ["cat" , "dog" ]:
    x = x / 4
else:
    x = x + 1
print (x)