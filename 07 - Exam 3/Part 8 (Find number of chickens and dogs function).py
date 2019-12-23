# a function that accepts two positive integers as parameters. The first integer is the number 
# of heads and the second integer is the number of legs of all the creatures in a farm which 
# consists of chickens and dogs. Your function should calculate and return the number of 
# chickens and number of dogs in the farm in a list as specified below. If it is impossible 
# to determine the correct number of chickens and dogs with the given information then your 
# function should return None. 

# Example 1, if your function received the following numbers:
# 5, 12 
# This means that someone has counted a total of 5 heads and total of 12 legs in the farm. 
# Now, your function should calculate how many chickens and how many dogs are in the farm 
# and return that information in a list exactly as shown below.
# [4, 1] 
# this means that there were 4 chickens and 1 dog in the farm.

# Example 2, if your function received the following numbers:
# 7, 12 
# Then it should return:
# None 



# Remember that you are not asked to print anything. So, your function should return a list that 
# contains two numbers exactly in this order [number_of_chickens, number_of_dogs] not print it. 
# You do not need to call your function, it will automatically be called and tested for correctness
# with the test cases we provide. You only need to write one function and we will test your program 
# with the first function that appears in your code. So, if you want to write more than one function 
# to help you solve the problem remember to embed the helper functions inside the first function.

# method 1
def CountAnimal1(Heads, Legs): 
    Dog = 0
    Dog = (Legs) - 2 * (Heads)
    if Dog < 0: 
        result = None
    else:
        Dog = Dog / 2
        Chicken = Heads - Dog
        if Chicken < 0: 
            result = None
        else:
            result = [int(Chicken), int(Dog)]        
    return result

# method 2
def CountAnimal2(head, leg):
    for chicken in range(1,head+1):
        for dog in range(1,head+1):
            if ((chicken*2) + (dog*4) == leg) and ((chicken + dog) == head):
                return [chicken, dog]

# Driver code test
heads = int(input("Please enter the heads number : "))
legs = int(input("Please enter the legs number : "))
result = CountAnimal2(heads, legs)
print("The number of chickens and dogs is :", result)

################### Sample Solution ###################
def _sample_fun_puzzle_ (heads,legs):
    dogs=(legs-heads*2)/2
    if dogs<0 or dogs%1:
        return None
    dogs=int(dogs)
    chickens=heads-dogs
    if chickens< 0:
        return None
    return [chickens,dogs]