# A program using while loop, which prints the sum of every third 
# numbers from 1 to 1001 ( both 1 and 1001 are included) 

# Type your code here
number = 1001
number_sum = 0
while (number >= 1):
    x = number % 3
    if x == 1:
        number_sum = number_sum + number
    number = number - 1
print(number_sum)

################### Sample Solution ###################
# x = 1
# count = 0
# while x < 1001:
#     count = count +x
#     x = x + 3
# print(count)