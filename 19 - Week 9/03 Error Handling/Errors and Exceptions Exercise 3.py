# What does the following program print? Choose the correct answer.

def dictionary_manipulation(my_dictionary, string, number):
    try:
        my_dictionary[string] = 2 * number - 1
    except (ValueError, KeyError):
        print("Error")
    else:
        my_dictionary[number+1] = string
    finally:
        print(my_dictionary)
 
# MAIN PROGRAM
dictionary_manipulation({}, "hello", 4)

# Options

# {7:'hello', 5: 'hello'}
# {8:'hello', 4: 'hello'}
# {'hello': 7, 5: 'hello'}      correct
# 'Error'
# {'hello': 7, 4: 'hello'} 