# A function which returns the number of words in the input string which 
# have more than 4 characters. Assume that the input string consists of 
# alphabetic characters separated by spaces and capitalization does not 
# matter i.e. an upper case character should be treated the same as a 
# lower case character. 

# Type your code here
def Count_Words_of_a_Length(String):
    String = String.lower().split()
    counter = 0
    for item in String:
        if len(item) > 4:
            counter += 1
    return counter

# Driver code tester
input_string = input("Please enter your string : ")
result = Count_Words_of_a_Length(input_string)
print(result)