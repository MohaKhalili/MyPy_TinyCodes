# A program to calculate the square root
# Babylonian Square Roots method

x = input("give me N, I will give you the Radical(N): ")
number = float(x)

guess = number /2       # First guess
error = 0.01            # The error between True and guess
iteration = 0           # Itertion of loop

while (abs(number - (guess ** 2)) > error):
    iteration = iteration + 1
    print(" -> on iteration",iteration,"my guess is",guess)
    taghsim = number / guess                    
    guess = (taghsim + guess) / 2               # new guess

print("The Square root of", number,"is",guess)