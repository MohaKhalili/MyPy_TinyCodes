# What does the following program print? If an Error occurs type 'Error' exactly without the quotes. 
# If None is printed type 'None' exactly without the quotes.
def evaluate_expression_1(x):
    x = x + 5
    def evaluate_expression_2(x):
        return x
    return x
scholar = 1008
print(evaluate_expression_1(scholar))

####################################################################################################
# What does the following program print? If an Error occurs type 'Error' exactly without the quotes. 
# If None is printed type 'None' exactly without the quotes.
def evaluate_expression_1():
    global x
    x = x + 5
    def evaluate_expression_2():
        return None
    return x
# Main Program #
x = 33
print(evaluate_expression_1())

####################################################################################################
# What does the following program print? If an Error occurs type 'Error' exactly without the quotes. 
# If None is printed type 'None' exactly without the quotes.
def evaluate_expression_1():
    global x
    x = x - 3
    def evaluate_expression_2():
        global x
        return x + 7
    return evaluate_expression_2()
# Main Program #
x = 33
print(evaluate_expression_1())

####################################################################################################
# What does the following program print? If an Error occurs type 'Error' exactly without the quotes. 
# If None is printed type 'None' exactly without the quotes.
def evaluate_expression_1(x):
    x = x - 3
    def evaluate_expression_2():
        global x
        return x + 7
    return evaluate_expression_2()
# Main Program #
x = 7
print(evaluate_expression_1(x))