# A program Using a for loop, a program which prints the 
# sum of all the even numbers from 1 to 101. 

# Type your code here
sum_iter = 0
for iter in range(1,102):
    if iter % 2 == 0:
        sum_iter = sum_iter + iter
print(sum_iter)
