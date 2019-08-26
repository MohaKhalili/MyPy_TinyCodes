#  a function that accepts two positive integers which are the height and width of 
# a rectangle and returns a list that contains the area and perimeter of that rectangle.

# Type your code here
def rectangle_area_peri(length,width):
    area = length * width
    perimeter = (length + width) * 2
    result = [area,perimeter]
    return result