# A function named list_to_tuples that receives a two dimensional 
# list of strings as parameter and returns a tuple of tuples where 
# the content of each inner list is reversed as shown below: 
# For example if the two dimensional list received by the 
# function is

# [['mean', 'really', 'is', 'jean'],
#  ['world', 'my', 'rocks', 'python']]

# Then, your function should return a tuple of tuples as shown below:

# (('jean', 'is', 'really', 'mean'), ('python', 'rocks', 'my', 'world'))

################### My Solution ###################
def list_to_tuples(MY_LIST):
    out_list = []
    for item in MY_LIST:
        inverse_list = []
        for index in range(len(item)):
            inverse_list.append(item[-1-index])
        out_list.append(tuple(inverse_list))
    return tuple(out_list)
        
################### Driver code ###################
test_list = [['mean', 'really', 'is', 'jean'],['world', 'my', 'rocks', 'python']]
result = list_to_tuples(test_list)
print(result)

################### Sample Solution ###################
def nested_list_to_nested_tuple(some_2d_list):
    for items in some_2d_list:
        items = items.reverse()
    for x in range(0, len(some_2d_list)):
        some_2d_list[x] = tuple(some_2d_list[x])
    return tuple(some_2d_list)