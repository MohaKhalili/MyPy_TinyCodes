# A function that accepts a tuple of positive integers and returns 
# the mean and median of the integers as a tuple. 
# 
# For example if the input tuple is:
# (3, 3, 0, 1, 12, 13, 15, 16)

# then your function should return a tuple that contains the mean and median as:
# (7.875, 7.5)

################### My Solution ###################
def Avg_Median(my_tuples):
    import numpy as np
    Median = np.median(list(my_tuples))
    Avg = np.mean(list(my_tuples))
    return (Avg,Median)

################### Driver code tester ###################
my_tuples = (3,5,1,9)
result = Avg_Median(my_tuples)
print(result)

################### Sample Solution ###################
def _statistics_with_a_tuple_sample_(sample_tuple):
    import numpy
    mean = sum(sample_tuple)/len(sample_tuple)
    median = numpy.median(numpy.array(sample_tuple))
    return mean, median