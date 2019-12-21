# There is 4 tiny question

# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match the 
# correct Python output.

m = 0
for x in range(1,4):
    for y in range(1,3):   
        m = m + 1
print (m)
##################################################################
m = 0
for x in range (1,3):
   for y in range (4,6):
      m = m + x + y
print (m)
##################################################################
m = 0
for x in range (1,3):
   k = 0
   for y in range (-2,0):
      k = k + y
      m = m + k
print (m)
##################################################################
m = 0
for x in [3,5,3]:
   for y in range (10,11):
      m = m + x + y
print (m)