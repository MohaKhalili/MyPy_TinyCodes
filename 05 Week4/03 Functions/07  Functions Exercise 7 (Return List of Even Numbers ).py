# a function which accepts an input list of numbers and returns a list which includes only 
# the even numbers in the input list. If there are no even numbers in the input numbers then
# your function should return an empty list.

# Type your code here
def even_between(list_number):
    MyList = []
    for i in range(len(list_number)):
        if list_number[i] % 2 == 0:
            MyList.append(list_number[i])
    return MyList