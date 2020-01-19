# What will be printed after each of the following code segments? 
# If error, then write Error

# Pay attention to the spaces. Your answer should exactly match 
# the correct Python output.

x = "mississipi" 
print (x[5:0:-2])
################################################################
x = "mississipi"
print (x.replace('s','z',2))
################################################################
my_str = "PYTHON"
print (my_str.ljust(8,'x'))
################################################################
my_str = "abcdecebacd"
print (my_str.rfind("c", 3, 10))
################################################################
x = "bye bob"
print (x.strip("b")) 
################################################################
x = ["dog", "cat", "pet"]
print ("ZZ".join(x))
################################################################
x = "hello hello"
print (x.count("h",1,7))
################################################################
x = "Cat Dog"
print (x.swapcase()) 
################################################################
x = "CSE"
print (x.center(9,"x")) 
################################################################
x = "CSE_1309"
print (x.index("0")) 