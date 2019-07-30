# a program to calculate the square root

def show_jazr(number):

    guess = number /2
    error = 0.01
    iteration = 0

    while (abs(number-guess**2) > error):
        iteration = iteration + 1
        #print("-> on iteration",iteration,"my guess is", guess)
        taghsim = number / guess
        guess = (taghsim + guess) / 2
    print("The square root of", number, "is", guess)

x = input("give me N, I will give you the Radical(N): ")
show_jazr(float(x))


show_jazr(50)
show_jazr(200)
 
