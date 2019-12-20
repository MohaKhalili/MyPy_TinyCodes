# a program that asks the user to enter a positive integer n. 
# Assuming that this integer is in seconds, your program should
# convert the number of seconds into days, hours, minutes, and 
# seconds and prints them exactly in the format specified below. 

# Type your code here
all_second = input("please enter a number:")
all_second = int(all_second)

s_days = 24*3600                                            # all second we have in a day
days_cal = all_second // s_days                             # Calculate the days
all_hour_Tosecond = all_second - (days_cal * s_days)        # remaining seconds after we get days
hour_cal = all_hour_Tosecond // (60 * 60)                   # Calculate the hours
all_minu_Tosecond = all_hour_Tosecond - (hour_cal * 3600)   # remaining seconds after we get hours
minu_cal = all_minu_Tosecond // 60                          # get the minutes
second_cal = all_minu_Tosecond - (minu_cal * 60)            # Finally calculate the remaining seconds after we get the minutes
print(days_cal,"days",hour_cal,"hours",minu_cal,"minutes",second_cal,"seconds")


################### Sample Solution ###################
# user_response = input("Enter a positive integer (seconds):")
# given_seconds = int(user_response)
# Calculate the days
# days = given_seconds//(24*60*60)
# seconds_1 = given_seconds % (24*60*60)    # remaining seconds after we get days

# Calculate the hours
# hours = seconds_1//(60*60)          # get the hours out of seconds_1
# seconds_2 = seconds_1 % (60*60)     # remaining seconds after we get hours

# Calculate the minutes
# minutes = seconds_2 // 60           # get the minutes

# Finally calculate the remaining seconds after we get the minutes
# seconds = seconds_2 % 60

# print(days, "days", hours, "hours", minutes, "minutes", seconds, "seconds")