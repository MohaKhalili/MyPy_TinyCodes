# A program to calculate the size of the pizza

# read radius
radius = input("please give me the radius: ")

#convert radius to number
radius_number = float(radius)

#calculate r^2
radius_power_two = radius_number * radius_number


pi = 3.1415 #everybody knows it

#calculate the area
pitza_area = radius_power_two * pi

if pitza_area < 100:
    print("very small pizza")
    print("are you sure you do not want another one?")
else:
    print("good, enjoy your pizza")

#print the output
print("The area of pizza is: ",pitza_area, "cm2")