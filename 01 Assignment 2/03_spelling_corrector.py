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
def spelling_corrector(s1,s2):
    new_string = ""
    correct_spells = s2
    string_splited = s1.split()
    print(string_splited)

# Definition required functions
    def find_mismatch(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        if len(s1) != len(s2):
            result = 2
        elif len(s1) == len(s2):
            count = 0
            for index in range(len(s1)):
                if s1[index] != s2[index]:
                    count = count + 1
            if count > 1:
                result = 2
            elif count == 1:
                result = 1
            else:
                result = 0
        return result
    def single_insert_or_delete(s1, s2):
        s1 = s1.lower()
        s2 = s2.lower()
        result = 0
        if len(s1) >= len(s2):
            max_string = s1
            min_string = s2
        else:
            max_string = s2
            min_string = s1
        if s1 != s2:
            result = 2
            if len(s1) != len(s2):
                if (max_string.replace(max_string[-1], "", 1) == min_string) or (
                        max_string.replace(max_string[0], "", 1) == min_string):
                    result = 1
                for index in range(min(len(s1), len(s2))):
                    if s1[index] != s2[index]:
                        max_string = max_string.replace(max_string[index], "", 1)
                        if max_string == min_string:
                            result = 1
                            break
                        max_string = max(s1, s2)
        return result

    for word in string_splited:
        if len(word) > 2:
            for word_correct_spells in correct_spells:
                if single_insert_or_delete(word_correct_spells, word) == 0:
                    new_string = new_string + word + " "
                    break
                elif single_insert_or_delete(word_correct_spells, word) == 1:
                    new_string = new_string + word_correct_spells + " "
                    break
                elif len(word) == 3 and word != word_correct_spells:
                    new_string = new_string + word + " "
                    break
        else:
            new_string = new_string + word + " "
    result = new_string.strip()
    return result

String = "Thes is the Firs cas"
correct_spells = ['that','first','case','car']
result = spelling_corrector(String, correct_spells)
print(result)