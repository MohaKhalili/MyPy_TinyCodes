# A function named capitalize_word_in_crossword that accepts a 2-dimensional 
# list of characters (like a crossword puzzle) and a string (word) as input 
# arguments. This function searches the rows and columns of the 2d list to 
# find a match for the word. If a match is found, this functions capitalizes 
# the matched characters in 2-dimensional list and returns the list. If no 
# match is found, this function simply returns the origianl 2-dimensional 
# list with no modification.

# Example 1: If the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','x','a','t'],['t','e','t','k']]
# word='cat'
# capitalize_word_in_crossword(crosswords,word)
# then your function should return:
# [['s','d','o','g'],['C','u','c','m'],['A','x','a','t'],['T','e','t','k']]
# Notice that the above list is a representation for a 2-dimensional crossword 
# puzzle as shown below.
# s	d	o	g
# C	u	c	m
# A	x	a	t
# T	e	t	k

# Example 2: if the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
# word='cat'
# capitalize_word_in_crossword(crosswords,word)
# then your function should return:
# [['s','d','o','g'],['c','u','c','m'],['a','C','A','T'],['t','e','t','k']]
# Notice that the above list is a representation for a 2-dimensional crossword 
# puzzle as shown below.
# s	d	o	g
# c	u	c	m
# a	C	A	T
# t	e	t	k

# Note: If both a horizontal and a vertical match is found then only select the 
# horizontal match. For example, in the above case there is a horizontal match 
# starting at [2,1] and there is also a veritcal match starting at [1,0]. Notice 
# that only the characters in the horizontal match should be capitalized in the 
# returned list.
# Hint: You should use the functions that you developed in part 1 and part 2 as 
# helper functions for part 3.

# Type your code here
def find_word_horizontal(crossword,word):
    # insert the code from your function in part 1 here
    result = None
    for index in range(len(list_2D)):
        list_test = ''.join(list_2D[index])
        if my_string in list_test:
            row = index
            for j in range(len(list_2D[index])):
                if my_string[0] == list_2D[index][j]:
                    col = j
                    result = [row, col]
                    break
            break
    return result


def find_word_vertical(crossword,word):
    # insert the code from your function in part 2 here
    for index in range(len(list_2D)):
        list_test = ''
        for j in range(len(list_2D)):
            list_test += list_2D[j][index]
            if my_string in list_test:
                col = index
                row = list_test.index(my_string[0])
                return [row, col]
    return None


def capitalize_word_in_crossword(crossword,word):


crossword=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
capitalize_word_in_crossword(crossword,word)