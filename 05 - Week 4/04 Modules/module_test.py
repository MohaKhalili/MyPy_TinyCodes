# Modules test

#########################
# First method
import SquareRoot

SquareRoot.show_square(213)
SquareRoot.show_square(23)
SquareRoot.show_square(98)
print("#########################")
#########################
# Second method
from SquareRoot import show_square

show_square(123)
show_square(432)
show_square(18)
print("#########################")
#########################
# square from math module
from math import sqrt
print(sqrt(600))
print("#########################")