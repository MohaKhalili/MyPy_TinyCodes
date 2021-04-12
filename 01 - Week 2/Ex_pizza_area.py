# A program to calculate the size of the pizza

# read radius
radius = input("please give me the radius: ")

#convert radius to number
radius_number = float(radius)

#calculate r^2
radius_power_two = radius_number * radius_number


pi = 3.14 #everybody knows it

#calculate the area
pitza_area = radius_power_two * pi

#print the output
print("The area of pizza is: ",pitza_area)
