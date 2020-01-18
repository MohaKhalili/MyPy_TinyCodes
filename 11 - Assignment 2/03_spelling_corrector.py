# a function named spelling_corrector that accepts two arguments.
# The first argument is a sentence (string) and the second argument
# is a list of words (correct_spells). Your function should check
# each word in the input string against all the words in the
# correct_spells list and return a string such that:
#
#     If a word in the original sentence matches exactly with a word in
#     the correct_spells then the word is not modified and it should be
#     directly copied to the output string.
#
#     if a word in the sentence can match a word in the correct_spells
#     list by replacing, inserting, or deleting a single character,
#     then that word should be replaced by the correct word in the
#     correct_spelled list.
#
#     If neither of the two previous conditions is true, then the word in
#     the original string should not be modified and should be directly
#     copied to the output string.
#
# Notes:
#
#     Do not spell check one or two letter words (copy them directly to the output string).
#     In case of a tie use the first word from the correct_spelled list.
#     Ignore capitalization, i.e. consider capital letters to be the same as lower case letters.
#     All characters in the output string should all be in lower case letters.
#     Assume that the input string only includes alphabetic characters and spaces. (a-z and A-Z)
#     Remove extra spaces between the words.
#     Remove spaces at the start and end of the output string.

def Spelling_corrector(input_string, input_list):

    input_string = input_string.split()
    output_string = ''

    def single_insert_or_delete(string1, string2):
        string1 = string1.lower()
        string2 = string2.lower()
        len_string1 = len(string1)
        len_string2 = len(string2)
        if string1 == string2:
            return 0
    
        if abs(len_string1-len_string2)!=1:
            return 2

        if max(len_string1, len_string2) == min(len_string1, len_string2)+1:
            if len_string1 > len_string2:
                maximum_string = string1
                minimum_string = string2
            else:
                maximum_string = string2
                minimum_string = string1
            test_string = ''
            for i in range(len(maximum_string)):
                test_string = maximum_string.replace(maximum_string[i],'',1)
                if test_string == minimum_string:
                    return 1
                    break
                test_string = ''
            return 2

    def find_mismatch(string1, string2):
        string1 = string1.lower()
        string2 = string2.lower()
        if string1 == string2:
            result = 0
        elif len(string1) == len(string2):
            counter = 0
            for i in range(len(string1)):
                if string1[i] != string2[i]:
                    counter += 1
            if counter == 1:
                result = 1
            else:
                result = 2
        else:
            result = 2
        return result

    for word in input_string:

        # Not checking one or two letter words (copy them directly to the output string).
        if len(word) <= 2:
            output_string += word
            if word != input_string[-1]:
                    output_string += " "
            continue
        
        # Then we check all the words in the list to find exactly the same word
        for item in input_list:

            result_find_mismatch = find_mismatch(word, item)                        # Calling find_mismatch function for the word of string and the word of list
            result_single_insert_or_delete = single_insert_or_delete(word , item)   # Calling single_insert_or_delete function for the word of string and the word of list
            counter = 0                                                             # initial value for flag of changes
            
            if result_find_mismatch == 0:               # if two words is the same
                output_string += word
                counter += 1                            # The flag is up, if the Change has occurred in this condition
                if word != input_string[-1]:            # added a space character, if the word is not the last one.
                    output_string += " "
                break  

        # If there are no words in the list that match the string word, so check words spelled for other cases
        if counter != 1:
            for item in input_list:

                result_find_mismatch = find_mismatch(word, item)                        # Calling find_mismatch function for the word of string and the word of list
                result_single_insert_or_delete = single_insert_or_delete(word , item)   # Calling single_insert_or_delete function for the word of string and the word of list
                counter = 0                                                             # initial value for flag of changes

                # if the two strings have the same length and mismatch in only one character.
                # or if the first string can become the same as the second string by inserting or deleting a single character. 
                if result_find_mismatch == 1 or result_single_insert_or_delete == 1:    
                    output_string += item
                    counter += 1                            # The flag is up, if the Change has occurred in this condition
                    if word != input_string[-1]:            # added a space character, if the word is not the last one.
                        output_string += " "
                    break                                   # break from this loop for choosen item
                
                # if the two strings have the same length and mismatch in only one character.
                # and if the two strings can become the same by Replacing one character
                elif result_find_mismatch == 1 and result_single_insert_or_delete == 2:
                    output_string += item
                    counter += 1                            # The flag is up, if the Change has occurred in this condition
                    if word != input_string[-1]:            # added a space character, if the word is not the last one.
                        output_string += " "
                    break                                   # break from this loop for choosen item

        # If none of the above conditions apply, move the word from the input string to the output string
        if counter == 0:
            output_string += word
            if word != input_string[-1]:            # added a space character, if the word is not the last one.
                output_string += " "
    return output_string


# driver code tester
String = "Asignment three xample inpu"
correct_spells = ['Assignmen', 'tree', 'three', 'example', 'output', 'input']
result = Spelling_corrector(String, correct_spells)
print(result)

################### Instructor function ###################
# def spelling_corrector (s,correct_spelled):
#     words=s.strip().split()
#     output_str=""
#     for current_word in words:
#         if len(current_word)<=2 or (current_word in correct_spelled) :
#             output_str=output_str+" "+current_word
#             continue
#         min_mismatch=2
#         replacement_word=current_word
#         for correct_word in correct_spelled:
#             if min(_find_mismatch(current_word,correct_word), _single_insert_or_delete(current_word,correct_word))==1:
#                 replacement_word=correct_word
#                 break
#         output_str=output_str+" "+replacement_word
#     return output_str.strip().lower()
# def _find_mismatch(s1,s2):
#     if len(s1) != len(s2):
#         return 2
#     s1=s1.lower()
#     s2=s2.lower()
#     number_of_mismatches=0
#     for index in range(len(s1)):
#         if s1[index] != s2[index]:
#             number_of_mismatches=number_of_mismatches+1
#             if number_of_mismatches>1:
#                 return 2
#     return number_of_mismatches 
# def _single_insert_or_delete(s1,s2):
#     s1=s1.lower()
#     s2=s2.lower()
#     if s1==s2:
#         return 0
#     if abs(len(s1)-len(s2))!=1:
#         return 2

#     if len(s1)>len(s2):
#         # only deletion is possible
#         for k in range(len(s2)):
#             if s1[k]!=s2[k]:
#                 if s1[k+1:]==s2[k:]:
#                     return 1
#                 else:
#                     return 2
#         return 1
#     else: # s1 is shorter Only insertion is possible
#         for k in range(len(s1)):
#             if s1[k]!=s2[k]:
#                 if s1[k:]==s2[k+1:]:
#                     return 1
#                 else:
#                     return 2
#         return 1