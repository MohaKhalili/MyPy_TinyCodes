# A function that takes an integer as input argument and returns the integer using 
# words. For example if the input is 4721 then the function should return the string 
# "four seven two one". Note that there should be only one space between the words and 
# they should be all lowercased in the string that you return.

# Type your code here
def Numbers_To_Words_dictionary(numbers):
    my_dict = {'0':'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    numbers = str(numbers)
    numbers = numbers.replace('',' ').split()
    my_string = ''
    for index in range(len(numbers)):
        my_string += my_dict[numbers[index]]
        if index != len(numbers)-1:
            my_string += " "
    return my_string

# driver code test
my_number = int(input("Please enter yoour number : "))
result = Numbers_To_Words_dictionary(my_number)
print(result)

################### Sample Solution ###################
def _single_digit_words_sample(sample_integer):
    string_input = str(sample_integer)      # convert the integer input into a string
    splitted = list(string_input)           # split the string into a list of characters
    sample_dictionary = {"1" : "one",
                         "2" : "two",
                         "3" : "three",
                         "4" : "four",
                         "5" : "five",
                         "6" : "six",
                         "7" : "seven",
                         "8" : "eight",
                         "9" : "nine",
                         "0" : "zero"}
    output_string = ""
    for integer in splitted:
        output_string += sample_dictionary[integer] + " "
    # remove any trailing whitespace
    stripped = output_string.rstrip(" ")
    return stripped