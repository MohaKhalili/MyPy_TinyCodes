# a program which asks the user to type an integer and then prints
# "Yes" if that integer is divisible by 3, otherwise prints "No"

# Type your code here
my_number = input("please enter your integer number : ")
my_number = int(my_number)
if (my_number%3)==0:
    print("Yes")
else:
    print("No")