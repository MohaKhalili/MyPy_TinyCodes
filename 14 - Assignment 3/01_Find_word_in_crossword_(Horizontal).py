# A function named find_word_horizontal that accepts a 2-dimensional list 
# of characters (like a crossword puzzle) and a string (word) as input arguments.
# This function searches the rows of the 2d list to find a match for the word. 
# If a match is found, this functions returns a list containing row index and 
# column index of the start of the match, otherwise it returns the value None 
# (no quotations).

# For example if the function is called as shown below:
# crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
# word='cat'
# find_word_horizontal(crosswords,word)

# then your function should return
# [2,1]

# Notice that the 2d input list represents a 2d crossword and the starting 
# index of the horizontal word 'cat' is [2,1]
# s d   o	g
# c	u	c	m
# a	c	a	t
# t	e	t	k
# Note: In case of multiple matches only return the match with lower row 
# index. If you find two matches in the same row then return the match with 
# lower column index. 

################### My function ###################
def find_word_horizontal(list_2D, my_string):
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

# driver code tester
crosswords=[['s','d','o','g'],['c','u','c','m'],['a','c','a','t'],['t','e','t','k']]
word='cat'
result = find_word_horizontal(crosswords,word)
print(result)

################### Instructor function ###################
def _find_word_horizontal(crosswords,word):
    if not crosswords or not word : # if empty then return None
        return None
    for index,row in enumerate(crosswords):
        temp_str=''.join(row)
        if temp_str.find(word)>=0:
            return [index,temp_str.find(word)]
    return None