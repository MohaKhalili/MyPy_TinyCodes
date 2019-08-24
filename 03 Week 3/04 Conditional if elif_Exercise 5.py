# a program which asks the user to type an integer.
# If the number is 2  then the program should print "two",
# If the number is 3  then the program should print "three",
# If the number is 5  then the program should print "five", 
# Otherwise it should print "other".

# Type your code here
my_num = input("please enter your number: ")
my_num = int(my_num)
if my_num == 2:
    print("two")
elif my_num == 3:
    print("three")
elif my_num == 5:
    print("five")
else:
    print("other")