# a program using while loop, which prints the sum of every third 
# numbers from 1 to 1001 ( both 1 and 1001 are included) 

# Type your code here
sum_iter = 0
for iter in range(1,102):
    if iter % 2 == 0:
        sum_iter = sum_iter + iter
print(sum_iter)
