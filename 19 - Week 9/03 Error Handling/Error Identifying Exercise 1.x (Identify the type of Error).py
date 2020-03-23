# Identify the type of Error that occurs when the following code is executed:

my_result = a * 8
# NameError

a = 12
b = 12-24
my_result = a/(a+b)
# ZeroDevisionError
    
a = 12
b = 13
my_result = (a + b / 2a)
# SyntaxError
    
a = 30
b = 74353634.89
my_result = a**b
# OverflowError
 
my_dictionary = {'tom': "Arnold",
                 'bob': "Henry",
                 'james':"Sulivan"}
print(my_dictionary["Henry"])
# KeyError