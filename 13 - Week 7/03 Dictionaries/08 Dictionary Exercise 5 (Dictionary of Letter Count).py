# A function that takes a string as input argument and returns a dictionary 
# of letter counts i.e. the keys of this dictionary should be individual letters 
# and the values should be the total count of those letters. You should ignore 
# white spaces and they should not be counted as a character. Also note that a 
# small letter character is equal to a capital letter character.

# method 1
def Dictionary_of_Letter_Count_method1(my_string):
    my_string = my_string.lower().replace(" ","")
    output_dict = {}
    for chara in my_string:
        output_dict[chara] = output_dict.get(chara, 0) + 1
    return output_dict

# method 2
def Dictionary_of_Letter_Count_method2(your_string):
    your_string = your_string.lower()
    splited_string = your_string.split()
    my_dict = {}
    for word in splited_string:
        for char in word:
            count = your_string.count(char)
            my_dict.setdefault(char, count)
    return my_dict

# driver code tester
string = input("Please enter your string : ")
result = Dictionary_of_Letter_Count_method1(string)
print(result)

################### Sample Solution ###################
# def _dictionary_of_letter_counts_sample_(sample_string):
#     stripped_string = sample_string.replace(" ", "")        # remove all white spaces
#     lowercase_stripped_string = stripped_string.lower()     # convert to lower case
#     sample_dictionary = {}
#     # Iterate through the lowercase stripped string and set each
#     # character as a key and its count as the value
#     for character in lowercase_stripped_string:
#         sample_dictionary[character] = lowercase_stripped_string.count(character)
#     return sample_dictionary