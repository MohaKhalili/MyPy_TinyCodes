# A function that calculates and returns the remaining loan balance. 
# This function accepts four parameters in the exact order shown below:

#        (principal, annual_interest_rate, duration , number_of_payments)
      

#    principal: The total amount of loan. Assume that the principal is positive floating point number.
#    annual_interest_rate: This is the percent interest rate per year. Assume that annual_interest_rate
#    is a floating point number. (Notice that 4.5 means that the interest rate is 4.5 percent per year.)
#    duration: number of years to pay the loan back. Assume that duration is a positive integer.
#    number_of_payments: number of monthly payments that are already paid. Assume that number_of_payments is an integer. 

# To calculate the reamining loan balance use the following equation
# RemainingLoanBalance=Principal∗(1+r)n−(1+r)p(1+r)n−1

# Where:
#    r is the monthly interest rate. r should be calculated by first dividing the annual_interest_rate by 100 and then divide the result by 12 to make it monthly. Notice that if the interest rate is equal to zero then the above equation will give you a ZeroDivisionError. In that case you should use the follwing equation: RemainingLoanBalance=Principal(1−pn)
#    n is the total number of monthly payments for the entire duration of the loan. Notice that n is equal to loan duration in years multiplied by 12.
#    p is the number of payments which are already made.

# Your function should return the remaining balance as a floating point number.

# Example: if your function is called with the following parameters:
# (1000.0,4.5,5,12)
# Then it should return a floating point number:
# 817.5512804582867
# Remember that you are not asked to print anything. So, your function should just return the resulting remaining balance.
# You do not need to call your function, it will automatically be called and tested for correctness with the test cases we 
# provide. You only need to write one function and we will test your program with the first function that appears in your 
# code. So, if you want to write more than one function to help you solve the problem remember to embed the helper function(s)
# inside the first function. 

#Type your code here
def Remaining_loan_balance(principal,annual_interest_rate,duration,number_of_payments):
    n = duration * 12
    p = number_of_payments
    if annual_interest_rate != 0:
        r = (annual_interest_rate / 100) / 12
        Remaining_loan_balance = (principal * ( ((1+r)**n) - ((1+r)**p) )) / (((1+r)**n) - 1)
    else:
        Remaining_loan_balance = principal * (1- (p/n))
    return Remaining_loan_balance

# Driver code test
principal = float(input("Please enter the all of loan value : "))
annual_interest_rate = float(input("Please enter the annual interest rate : "))
duration = int(input("Please enter the loan payment duration : "))
number_of_payments = int(input("Please enter the number of payments : "))
result = Remaining_loan_balance(principal,annual_interest_rate,duration,number_of_payments)
print(result)