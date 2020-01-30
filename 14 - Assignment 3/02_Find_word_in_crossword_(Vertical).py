# A function named find_word_vertical that accepts a 2-dimensional 
# list of characters (like a crossword puzzle) and a string (word) 
# as input arguments. This function searches the columns of the 2d 
# list to find a match for the word. If a match is found, this 
# functions returns a list containing row index and column index of 
# the start of the match, otherwise it returns the value None (no 
# quotations).

# For example if the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
# word='cat'
# find_word_vertical(crosswords,word)

# then your function should return:
# [1,0]

# Notice that the 2d input list represents a 2d crosswords and the 
# starting index of the vertical word 'cat' is [1,0]
# s	d	o	g
# c	u	c	m
# a	c	a	t
# t	e	t	k
# Note: In case of multiple matches only return the match with lower 
# column index. If you find two matches in the same column then return the match with lower row index.
# Code Editor

################### My function ###################
def find_word_vertical(list_2D, my_string):
    for index in range(len(list_2D)):
        list_test = ''
        for j in range(len(list_2D)):
            list_test += list_2D[j][index]
            if my_string in list_test:
                col = index
                row = list_test.index(my_string[0])
                return [row, col]
    return None

# driver code tester
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
result = find_word_vertical(crosswords,word)
print(result)

################### Instructor function ###################
def _find_word_vertical(crosswords,word):
    if not crosswords or not word:
        return None    
    number_of_columns=len(crosswords[0])
    for col_index in range (number_of_columns):
        temp_str=''
        for row_index in range(len(crosswords)):
            temp_str=temp_str+crosswords[row_index][col_index]
        if temp_str.find(word)>=0:
            return [temp_str.find(word),col_index]
    return None