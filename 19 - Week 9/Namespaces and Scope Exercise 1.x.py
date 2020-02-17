# What does the following program print? If an Error occurs type 'Error' exactly without the quotes.

def test():
    x=7
# Main Program #
x = 11
test()
print(x)

####################################################################################################
# What does the following program print? If an Error occurs type 'Error' exactly without the quotes. 
# If None is printed type 'None' exactly without the quotes.
def test():
    global x
    x=7
# Main Program #
x = 11
test()
print(x)

####################################################################################################
# What does the following program print? If an Error occurs type 'Error' exactly without the quotes. 
# If None is printed type 'None' exactly without the quotes.
def test(x):
    x=8
# Main Program #
x = 5
test(x)
print(x)

####################################################################################################
# What does the following program print? If an Error occurs type 'Error' exactly without the quotes. 
# If None is printed type 'None' exactly without the quotes.
def test(x):
    x = 7
# Main Program #
x = 11
x = test(x)
print(x)