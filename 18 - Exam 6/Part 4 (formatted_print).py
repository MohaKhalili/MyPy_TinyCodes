# A function named formatted_print that receives a dictionary as argument. 
# The keys of the dictionary will be the names of the students and the values 
# of the dictionary will be their average scores. Your function should print 
# this information exactly as specified below :

# For example if the dictionary received by the function is
# {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900} 

# Then your function should print:
# alex       90.55
# eva        88.50
# tim        65.90
# john       34.48

# Note:
#     The names have to be accommodated within 10 spaces and they are left justified.
#     
#     The scores are floats and they should be right justified in 6 spaces with two 
#     digits after the decimal point.
#     
#     All this information has to be sorted (descending order) by the scores of the 
#     students. Notice how alex has the highest score and appears first and john has 
#     the lowest score and appears last.

################### My Solution ###################
def formatted_print(my_dictionary):
    
    dict_values = sorted(list(my_dictionary.values()), reverse=True)

    # function to return key for any value 
    def get_key(val): 
        for key, value in my_dictionary.items(): 
            if val == value: 
                return key 

    for item in dict_values:
        string = "{0:<10}{1:>6.2f}".format(get_key(item), item)
        print(string)

################### Driver Code ###################
my_dict = {'john':34.480, 'eva':88.5, 'alex':90.55, 'tim': 65.900}
result = formatted_print(my_dict)

################### Sample Solution ###################
def dict_to_print(a):
    my_names = list(a.keys())
    my_scores = list(a.values())
    
    # Sort the information by score descending order
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, len(my_scores)-1):
            # if next element is greater element then swap them
            if my_scores[index] < my_scores[index + 1]:
                # sort the scores
                temporary_score = my_scores[index]
                my_scores[index] = my_scores[index + 1]
                my_scores[index + 1] = temporary_score
                # sort the names as well 
                temporary_name = my_names[index]
                my_names[index] = my_names[index + 1]
                my_names[index + 1] = temporary_name               
                
                unSorted = True    
    for x in range(0, len(my_names)):
        print("{0:<10s}{1:>6.2f}".format(my_names[x], my_scores[x]))