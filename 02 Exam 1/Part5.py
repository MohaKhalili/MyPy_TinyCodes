# a program that asks the user for a positive integer between
# 1 and 7 (Assume that the user may enter any number from 1 to 7
# both inclusive) and prints the day of week corresponding to that
# number in all capital letters. Assume that the day of the week 
# starts from MONDAY. 

# Type your code here
x = input("please enter a number from 1 to 7: ")
week_list = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY','SUNDAY']
x = int(x)
x=x-1
print(week_list[x])