# A function that a accepts a positive number 'r' as the radius of a circle and 
# calculates and returns the area of the circle. Use the value of pi as 3.14

# Type your code here
def circle_area(r):
    r = abs(r)
    area = 3.14 * (r**2)
    return area

# Driver code test
number = float(input("Please enter the radius : "))
result = circle_area(number)
print(result)