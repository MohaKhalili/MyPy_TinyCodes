# What does the following program print? Choose the correct answer.

def dictionary_manipulation(my_dictionary, string, number):
    try:
        my_dictionary[string] = 2 * number
    except (ValueError, KeyError):
        print("Error")
    else:
        my_dictionary[number+1] = 2 * string
    finally:
        print(my_dictionary)
 
# MAIN PROGRAM
dictionary_manipulation({"first":1, "second":2},"last", 8)

# Options:

# {4:'last', 'first': 1, 'second': 2, 9: 'lastlast'}
# {'last': 16, 9: 'lastlast', 'second': 2, 'first': 1}      correct
# {'last': 8, 'first': 1, 'second': 2, 9: 'lastlast'}
# {'last': 4, 'first': 1, 'second': 2, 16: 'lastlast'} 