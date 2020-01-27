# A function named "reverse_dictionary" that receives a dictionary as input 
# argument and returns a reverse of the input dictionary where the values of 
# the original dictionary are used as keys for the returned dictionary and 
# the keys of the original dictionary are used as value for the returned 
# dictionary as explained below:

# For example, if the function is called as :
# reverse_dictionary({'Accurate': ['exact', 'precise'], 'exact': ['precise'],
# 'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']})

# then your function should return
# {'precise': ['accurate', 'exact'], 'clever': ['astute', 'smart'], 'talented': ['smart'],
#  'bright': ['smart'], 'exact': ['accurate'], 'smart': ['astute']}

# Notes:
#   The list of values in the returned dictionary is sorted in ascending order.

#   Capitalization does not matter. This means that all the words should be 
#   converted to lower case letters. For example the word "Accurate" is capitalized 
#   in the original dictionary but in the returned dictionary it is written with all 
#   lower case letters.

# my function for inverting dictionaries
def reverse_dictionary(my_dict):
    my_inverted_dict = {}
    for key, value in my_dict.items():
        for element in value:
            my_inverted_dict.setdefault(element.lower(), list()).append(key.lower())
    final_dict = {}
    for key, value in my_inverted_dict.items():
        final_dict.setdefault(key, sorted(value))
    return final_dict

my_dictionary = {'Accurate': ['exact', 'precise'], 'exact': ['precise'],'astute': ['Smart', 'clever'], 'smart': ['clever', 'bright', 'talented']}
result = reverse_dictionary(my_dictionary)
print(result)

################### Instructor function ###################
def _reverse_dictionary(input_dict):
    output_dict={}
    for k in input_dict:        
        for value in input_dict[k]:
            key_lowered=k.lower()
            value_lowered=value.lower()
            if output_dict.get(value_lowered):
                if k not in output_dict[value_lowered]:
                    output_dict[value_lowered].append(key_lowered)
                    output_dict[value_lowered].sort()
            else:
                output_dict[value_lowered]=[key_lowered]
    return output_dict