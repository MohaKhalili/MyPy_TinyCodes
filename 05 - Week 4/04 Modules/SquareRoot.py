# Square root module with babylonian method
def show_square(number):

    guess = number /2
    error = 0.01
    iteration = 0

    while (abs(number-guess**2) > error):
        iteration = iteration + 1
        #print("-> on iteration",iteration,"my guess is", guess)
        taghsim = number / guess
        guess = (taghsim + guess) / 2
    print("The square root of", number, "is", guess)