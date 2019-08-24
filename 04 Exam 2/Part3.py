# a program which asks the user to enter their age in years 
# (Assume that the user always enters an integer) and based on
# the following conditions, prints the output exactly as in the
# following format (as highlighted in yellow):

# When age is less than or equal to 0, your program should print
# UNBORN

# When age is greater than 0 and less than or equal to 150, 
# your program should print
# ALIVE

# When age is greater than 150, your program should print
# VAMPIRE

# Type your code here
your_year = input("please enter your year:" )
your_year = int(your_year)
if your_year <= 0:
    print("UNBORN")
elif your_year > 0 and your_year <= 150:
    print("ALIVE")
else:
    print("VAMPIRE")
