# A function named n_letter_dictionary that receives a string (words separated by spaces) 
# as parameter and returns a dictionary whose keys are numbers and whose values are lists 
# that contain unique words that have the number of letters equal to the keys.

# For example, when your function is called as:

# n_letter_dictionary("The way you see people is the way you treat them and the Way you treat 
# them is what they become")

# Then, your function should return a dictionary such as

# {2: ['is'], 3: ['and', 'see', 'the', 'way', 'you'], 4: ['them', 'they', 'what'], 5: ['treat'], 6: ['become', 'people']}

# Notes:

#     Each list of words with the same number of letters should be sorted in ascending order
#     The words in a list should be unique. For example, even though the word "them" is repeated twice in the above sentence, it is only considered once in the list of four letter words.
#     Capitalization does not matter, this means that all the words should be converted to lower case. For example the words "The" and "the" appear in the sentence but they are both considered as lower case "the". 

# Do NOT import any module for solving this problem.

################### My Solution ###################
def n_letter_dictionary(my_string):
    my_string = my_string.lower().split()
    output_dict = {}
    new_list = []
    for i in range(len(my_string)):
        if my_string[i] not in new_list:
            new_list.append(my_string[i])
            output_dict.setdefault(len(new_list[-1]), list()).append(new_list[-1])
            output_dict.setdefault(len(new_list[-1]), list()).sort()
    return output_dict

################### Driver Code ###################
my_string = "The way you see people is the way you treat them and the Way you treat them is what they become"
result = n_letter_dictionary(my_string)
print(result)

################### Sample Solution ###################
def n_letter_dictionary_final_sp(my_string):
    my_dict = {}
    my_list = my_string.strip().split()
    for word in my_list:
        length=len(word)
        lowered_word=word.lower()
        if my_dict.get(length):
            if lowered_word not in my_dict[length]:
                my_dict[length].append(lowered_word)
                my_dict[length].sort()
        else:
            my_dict[length]=[lowered_word]
    return my_dict