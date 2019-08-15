# a function that takes a string consisting of alphabetic
# characters as input argument and returns the lower case
# of the most common character. Ignore white spaces i.e.
# Do not count any white space as a character. Note that
# capitalization does not matter here i.e. that a lower
# case character is equal to a upper case character. In
# case of a tie between certain characters return the last
# character that has the most count Code Editor
def Most_Common_Character(String):
    stripped_string = String.replace(" ", "")    # remove all white spaces
    lowercase_stripped_string = stripped_string.lower()    # convert to lower case
    sample_character = None
    sample_maximum_count = 0

    # Iterate through the given string and for each character
    # set a count, among these counts,  return the character whose count is maximum
    # On case of tie, return the last character that occurs that has the most count
    for character in lowercase_stripped_string:
        each_character_count = lowercase_stripped_string.count(character)
        if each_character_count >= sample_maximum_count:
            sample_maximum_count = each_character_count
            sample_character = character
    return sample_character

# driver code test
char = "hello mohammad, how are you?"
result = Most_Common_Character(char)
print(result)