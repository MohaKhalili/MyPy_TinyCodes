# a program that asks the user to enter their age in years 
# as input (assume that the user enters a positive integer) 
# and calculates and prints how old the user is in terms of
# days. Assume that there are 365 days in a year.

# Type your code here
age_year = input("please enter your age: ")
age_day = int(age_year) * 365

print("You are", age_day,"days old")