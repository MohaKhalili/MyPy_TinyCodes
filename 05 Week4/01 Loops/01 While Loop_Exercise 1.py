# a program which prints the sum of numbers from 1 to 101
# that are divisible by 5. ( 1 and 101 are included) (Use while loop)

# Type your code here
number = 101
number_sum = 0
while (number >= 1):
    x = number % 5
    if x == 0:
        number_sum = number_sum + number
    number = number - 1
print(number_sum)
