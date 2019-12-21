# A program using while loop, which asks the user to type a 
# positive integer, n, and then prints the factorial of n. 
# A factorial is defined as the product of all the numbers 
# from 1 to n (1 and n inclusive). For example factorial of
# 4 is equal to 24. (because 1*2*3*4=24)

# Type your code here
n = input("please enter N number,then i will give you N factoriel: ")
n = int(n)
factoriel_N = 1
while n > 0:
    factoriel_N = factoriel_N * n
    n = n - 1
print(factoriel_N)

################### Sample Solution ###################
# y = input("Type a number:")
# x = int(y)
# count = 1
# z = 1
# while z <= x:
#     count = count * z
#     z = z + 1
# print(count)