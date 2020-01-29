# A function that accepts a string which contains a particular 
# date from the Gregorian calendar. Your function should return 
# what day of the week it was. Here are a few examples of what 
# the input string(Month Day Year) will look like. However, you 
# should not 'hardcode' your program to work only for these input!

# "June 12 2012"
# "September 3 1955"
# "August 4 1843" 

# Note that each item (Month Day Year) is separated by one space. 
# For example if the input string is:
# "May 5 1992"
# Then your function should return the day of the week (string) such as:
# "Tuesday"

# Algorithm with sample example:
# # Assume that input was "May 5 1992"
# day (d) = 5        # It is the 5th day
# month (m) = 3      # (*** Count starts at March i.e March = 1, April = 2, ... January = 11, February = 12)
# century (c) = 19   # the first two characters of the century
# year (y) = 92      # Year is 1992 (*** if month is January or february decrease one year)
# # Formula and calculation
# day of the week (w) = (d + floor(2.6m - 0.2) - 2c + y + floor(y/4) + floor(c/4)) modulo 7
# after calculation we get, (w) = 2
# Count for the day of the week starts at Sunday, i.e Sunday = 0, Monday = 1, Tuesday = 2, ... Saturday = 6
# Since we got 2, May 5 1992 was a Tuesday

################### MY FUNCTIION ###################
def Day_of_the_Week(date_string):
    
    import math
    
    month_dict = {'March':1, 'April':2, 'May':3, 'June':4, 'July':5, 'August':6, 'September':7, 'October':8, 'November':9, 'December':10, 'January':11, 'February':12}
    week_dict = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

    date_list = date_string.split()
    for index in range(len(date_list)):
        if index == 0:
            month = month_dict[date_list[index]]
        elif index == 1:
            day = int(date_list[index])
        else:
            century = date_list[index]
            century = int(century[0:2])
            year = date_list[index]
            year = int(year[2:])
            if month == 11 or month == 12:
                year = year - 1           

    w = (day + math.floor(2.6*month - 0.2) - 2*century + year + math.floor(year/4) + math.floor(century/4)) % 7

    return week_dict[w]

# driver code
your_string = input("Please enter your date string : ")
result = Day_of_the_Week(your_string)
print(result)

################### Sample Solution ###################
def _day_of_the_week_sample_(string):
    import math
    my_month, day, year = string.split(" ")
    months = {"March": 1,
              "April": 2,
              "May": 3,
              "June": 4,
              "July": 5,
              "August": 6,
              "September": 7,
              "October": 8,
              "November": 9,
              "December": 10,
              "January": 11,
              "February": 12}
    weeks = {"Sunday": 0,
            "Monday": 1,
            "Tuesday": 2,
            "Wednesday": 3,
            "Thursday": 4,
            "Friday": 5,
            "Saturday": 6}
    # Get the appropriate month as an int using a dictionary
    month = months[my_month]
    day = int(day)
    # The first two characters of the year
    century = int(year[0] + year[1])
    # The last two characters of the year
    year = int(year[2] + year[3])
    # If month > 10 (i.e january or february then substract one year)
    if month > 10:
        year = year - 1
    # Calculation
    w = (day + math.floor(2.6*month - 0.2) -2*century + year + math.floor(year/4) + math.floor(century/4))%7
    for day in weeks:
        if weeks[day] == w:
            return day