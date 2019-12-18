# a program which asks the user to type a string and then: 
# Print "Dog" if the word "dog" exists in the input string.
# Print "Cat" if the word "cat" exists in the input string.
# (if both "dog" and "cat" exist in the input string, then 
# you should only print "Dog") 
# Otherwise prints "None". (Pay attention to capitalization).

# Type your code here
my_str = input("please enter your string : ")
if "dog" in my_str:
    print("Dog")
elif "cat" in my_str:
    print("Cat")
elif "dog" in my_str and "cat" in my_str:
    print("Dog")
else:
    print("None")

################### Sample Solution ###################
# user_response=input("Type anything:")
# if 'dog' in user_response:
#    print ('Dog')
# elif 'cat' in user_response:
#     print ('Cat')
# else:
#     print ('None')