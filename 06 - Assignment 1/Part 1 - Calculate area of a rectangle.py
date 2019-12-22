# A function that accepts two positive integers which are the height 
# and width of 

# A rectangle and returns a list that contains the area and perimeter 
# of that rectangle.

# Type your code here
def rectangle_area_peri(length,width):
    area = length * width
    perimeter = (length + width) * 2
    result = [area,perimeter]
    return result

# Driver code test
length = int(input("Please enter the length of rectangle : "))
width = int(input("Please enter the width of rectangle : "))
result = rectangle_area_peri(length,width)
print("The rectangle area is : ",result[0], "The rectangle perimeter is : ",result[1])