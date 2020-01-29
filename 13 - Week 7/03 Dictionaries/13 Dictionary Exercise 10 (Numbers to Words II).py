# Write a function that takes a 4 digit integer (from 1000 to 9999 both inclusive) as input argument and returns the integer using words as shown below:

# Sample Examples:
# if the input integer is 7000 then the function should return the string "seven thousand"
# if the input integer is 1008 then the function should return the string "one thousand eight"
# if the input integer is 4010 then the function should return the string "four thousand ten"
# if the input integer is 1012 then the function should return the string "one thousand twelve"
# if the input integer is 4506 then the function should return the string "four thousand five hundred six"
# if the input integer is 9900 then the function should return the string "nine thousand nine hundred"
# if the input integer is 8880 then the function should return the string "eight thousand eight hundred eighty"
# if the input integer is 5432 then the function should return the string "five thousand four hundred thirty two"

# Notice that the words in the output strings should all be lower cased and separated by only one space and make sure your words match the following spellings:

# one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen,
# sixteen, seventeen, eighteen, nineteen, twenty, thirty, forty, fifty, sixty, seventy, eighty,
# ninety, hundred, thousand

################### MY FUNCTION ###################
def Numbers_to_Words_II(number):

    dict_1to19 =  {'1':'one', '2':'two', '3':'three', '4':'four', 
                    '5':'five', '6':'six', '7':'seven', '8':'eight', 
                    '9':'nine', '10':'ten', '11':'eleven', '12':'twelve', 
                    '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', 
                    '17':'seventeen', '18':'eighteen', '19':'nineteen'}

    dict_20to90 = {'20':'twenty', '30':'thirty', '40':'forty', '50':'fifty', '60':'sixty', '70':'seventy', '80':'eighty', '90':'ninety'}

    
    number_string = str(number)

    for index in range(len(number_string)):
        if index == 0:
            output_string = dict_1to19[number_string[index]] + ' ' + 'thousand'
            if int(number_string[1:]) == 000:
                break
        elif index == 1:
            if int(number_string[index]) != 0:
                output_string += ' ' + dict_1to19[number_string[index]] + ' ' + 'hundred'
        else:
            if int(number_string[2:]) == 00:
                break
            if int(number_string[-2]) == 0:
                output_string += ' ' + dict_1to19[number_string[-1]]
                break
            elif int(number_string[2:]) <= 19:
                output_string += ' ' + dict_1to19[number_string[2:]]
                break
            elif int(number_string[2:]) > 19:
                if int(number_string[2:]) % 10 == 0:
                    output_string += ' ' + dict_20to90[number_string[2:]]
                    break
                else:
                    dahgan_ID = int(number_string[2:]) // 10
                    output_string += ' ' + dict_20to90[str(dahgan_ID*10)]
                    yekan = int(number_string[2:]) - (dahgan_ID*10)
                    output_string += ' ' + dict_1to19[str(yekan)]
                    break
    return output_string

# driver code
my_number = int(input("Please enter your number : "))
result = Numbers_to_Words_II(my_number)
print(result)

################### Sample Solution ###################
def _single_digit_words_sample(sample_integer):
    # Note that this is just one way
    # of solving this problem
    # It can be solved in many different ways
    string_input = str(sample_integer)      # convert the integer input into a string
    splitted = list(string_input)           # split the string into a list of characters
    sample_dictionary = {"0" : ["zero", ""],
                         "1" : ["one", ""],
                         "2" : ["two","twenty"],
                         "3" : ["three","thirty"],
                         "4" : ["four","forty"],
                         "5" : ["five","fifty"],
                         "6" : ["six","sixty"],
                         "7" : ["seven","seventy"],
                         "8" : ["eight","eighty"],
                         "9" : ["nine","ninety"],
                         "10" : "ten",
                         "11" : "eleven",
                         "12" : "twelve",
                         "13" : "thirteen",
                         "14" : "fourteen",
                         "15" : "fifteen",
                         "16" : "sixteen",
                         "17" : "seventeen",
                         "18" : "eighteen",
                         "19" : "nineteen"}

    thousand_digit = sample_dictionary[splitted[0]][0]
    hundred_digit = sample_dictionary[splitted[1]][0]
    ten_digit = sample_dictionary[splitted[2]][0]
    one_digit = sample_dictionary[splitted[3]][0]

    my_list = []
    # Work with the thousand digit
    my_list.append(thousand_digit)
    my_list.append("thousand")

    if hundred_digit != "zero":
        my_list.append(hundred_digit)
        my_list.append("hundred")

    if ten_digit == "zero" and one_digit != "zero":
        my_list.append(one_digit)

    if ten_digit != "zero" and one_digit == "zero":
        ity_digit = sample_dictionary[splitted[2]][1]
        my_list.append(ity_digit)

    if ten_digit != "zero" and ten_digit != "one" and one_digit != "zero":
        ity_digit = sample_dictionary[splitted[2]][1]
        my_list.append(ity_digit)
        last_digit = sample_dictionary[splitted[3]][0]
        my_list.append(last_digit)

    if ten_digit != "zero" and ten_digit == "one" and one_digit != "zero":
        last_two_digits = sample_dictionary[splitted[2]+splitted[3]]
        my_list.append(last_two_digits)

    if ten_digit != "zero" and ten_digit == "one" and one_digit == "zero":
        last_two_digits = sample_dictionary[splitted[2]+splitted[3]]
        my_list.append(last_two_digits)

    # remove any "" that the list contains
    # due to the way the program was implemented
    if "" in my_list:
        my_list.remove("")
    out_string = ""
    out_string = ' '.join(my_list)
    return out_string