# What does the following program print? If an Error occurs type 'Error' exactly without the quotes.

def perform_multiplication(integer_1, integer_2):
    integer_2 = integer_1 * integer_2
    return integer_1, integer_2

# Main Program #
integer_1, integer_2 = perform_multiplication(8, 11)
print(integer_1, integer_2)