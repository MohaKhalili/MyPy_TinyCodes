# a function that accepts a string and a character as input
# and returns the count of all the words in the string which
# start with the given character. Assume that capitalization
# does not matter here.
def Count_Words_Starting_With_a_Character(String, char):
    # Instantiate a variable for counting
    count = 0
    if char.isupper():
        String = String.upper()
    else:
        String = String.lower()
    # Create a list of strings by splitting the original string
    String = String.split()
    # Iterate through each string in the list that was produced
    # and check if the first character of each string is equal
    # to the template character. If it does increase the
    # count by 1 and finally return the count
    for i in String:
        if i[0] == char:
            count = count + 1
    return count

# driver code test
String = "hello MOHAMMAD mohammad"
char = "M"
result = Count_Words_Starting_With_a_Character(String, char)
print(result)