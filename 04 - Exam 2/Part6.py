# a program that asks the user to enter a positive integer n. 
# Assuming that this integer is in seconds, your program should
# convert the number of seconds into days, hours, minutes, and 
# seconds and prints them exactly in the format specified below. 

# Type your code here
n = input("please enter an time (second): ")
n = int(n)
total_amount = 24*60*60
if n >= total_amount:
    day = n // total_amount
    hour = (n - day * total_amount) // 3600
    minu = (n - day * total_amount - hour * 3600) // 60
    second = (n - day * total_amount - hour * 3600 - minu * 60)
    print(day,"days",hour,"hours",minu,"minutes",second,"seconds")
else:
    day = n // total_amount
    hour = n // 3600
    minu = (n - hour * 3600) // 60
    second = (n - hour * 3600 - minu * 60)
    print(day,"days",hour,"hours",minu,"minutes",second,"seconds")