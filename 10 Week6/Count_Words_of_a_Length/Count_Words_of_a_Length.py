#  a function which returns the number of words in the input
#  string which have more than 4 characters. Assume that the
#  input string consists of alphabetic characters separated
#  by spaces and capitalization does not matter i.e. an upper
#  case character should be treated the same as a lower case
#  character.

def Count_Words_of_a_Length(String):
    # Create a list of strings by splitting the original string
    String = String.lower().split()
    count = 0
    # Go through each string in the list we created
    for char in String:
        # check the length of each string
        # it resets for each string
        if len(char) > 4:
            count = count + 1
    return count

# driver code test
String = "hello MOHAMMAD jan"
result = Count_Words_of_a_Length(String)
print(result)