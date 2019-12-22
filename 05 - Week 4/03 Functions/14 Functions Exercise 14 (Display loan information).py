# A program for loan calculations. Your program should ask the user for three pieces of 
# information (with three seperate input() functions:)

#    Total amount of loan.
#    Annual interest rate. (Assume that the interest rate is a positive integer. For example 5 means
#    that annual interest is 5% (five percent) per year.
#    Total duration of loan in years.

# Your Program should use the two functions that you implented in part 1 and 2 of this exercise and 
# display the follwoing information about the loan.

#    In the first first line show the amount of loan and interest rate.
#    In the second line show duration of the loan and monthly payment.
#    In each of the following lines show the Loan balance and total amount paid for each year.

# Example 1: assuming that user inputs the following numbers in response to your questions:

# Enter loan amount: 1000.0
# Enter annual interest rate (percent): 10.0
# Enter loan duration in years: 5

    

# The output of your program should be:

# LOAN AMOUNT: 1000 INTEREST RATE (PERCENT): 10
# DURATION (YEARS): 5 MONTHLY PAYMENT: 21
# YEAR: 1 BALANCE: 837 TOTAL PAYMENT 254
# YEAR: 2 BALANCE: 658 TOTAL PAYMENT 509
# YEAR: 3 BALANCE: 460 TOTAL PAYMENT 764
# YEAR: 4 BALANCE: 241 TOTAL PAYMENT 1019
# YEAR: 5 BALANCE: 0 TOTAL PAYMENT 1274

  
# Important notes:
#  * Use floating point numbers in your calculations.
#  * Convert all the numbers to int only for printing them. 

# # Your function for calculating payment goes here
# def Mounthly_payment(principal, annual_interest_rate, duration):
#     n = duration * 12
#     if annual_interest_rate != 0:
#         r = (annual_interest_rate / 100) / 12
#         Mounthly_payment = (principal * (r * ((1+r)**n))) / (((1+r)**n) - 1)
#     else:
#         Mounthly_payment = principal / n
#     return Mounthly_payment


# # Your function for calculating remaining balance goes here
# def Remaining_loan_balance(principal,annual_interest_rate,duration,number_of_payments):
#     n = duration * 12
#     p = number_of_payments
#     if annual_interest_rate != 0:
#         r = (annual_interest_rate / 100) / 12
#         Remaining_loan_balance = (principal * ( ((1+r)**n) - ((1+r)**p) )) / (((1+r)**n) - 1)
#     else:
#         Remaining_loan_balance = principal * (1- (p/n))
#     return Remaining_loan_balance         

# # Your main program goes here
# principal=float(input("Enter loan amount: "))
# annual_interest_rate=float(input("Enter annual interest rate (percent): "))
# duration=int(input("Enter loan duration in years: "))

# print("LOAN AMOUNT:",int(principal),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
# print("DURATION (YEARS):",duration,"MONTHLY PAYMENT:",int(Mounthly_payment(principal,annual_interest_rate,duration)))

# for i in range(1,duration+1):
#     BALANCE = Remaining_loan_balance(principal,annual_interest_rate,duration,i*12)
#     TOTAL_PAYMENT = i*12*Mounthly_payment(principal,annual_interest_rate,duration)
#     print("YEAR:",i,"BALANCE:",int(BALANCE),"TOTAL PAYMENT",int(TOTAL_PAYMENT))


def Loan_Information(loan_amount, annual_interest_rate, duration):

    def MP_loan_calc(principal, annual_interest_rate, duration):
        n = duration * 12
        if annual_interest_rate != 0:
            r = (annual_interest_rate / 100) / 12
            Mounthly_payment = (principal * (r * ((1+r)**n))) / (((1+r)**n) - 1)
        else:
            Mounthly_payment = principal / n
        return Mounthly_payment

    def Remaining_loan_balance(principal,annual_interest_rate,duration,number_of_payments):
        n = duration * 12
        p = number_of_payments
        if annual_interest_rate != 0:
            r = (annual_interest_rate / 100) / 12
            Remaining_loan_balance = (principal * ( ((1+r)**n) - ((1+r)**p) )) / (((1+r)**n) - 1)
        else:
            Remaining_loan_balance = principal * (1- (p/n))
        return Remaining_loan_balance

    result_MP_loan_calc = MP_loan_calc(loan_amount, annual_interest_rate, duration)
    
    print ("LOAN AMOUNT:",int(loan_amount),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
    print("DURATION (YEARS):",int(duration),"MONTHLY PAYMENT:",int(result_MP_loan_calc))

    for i in range(1,duration+1):
        result_Remaining_loan_balance = Remaining_loan_balance(loan_amount,annual_interest_rate,duration,i*12)
        TOTAL_PAYMENT = result_MP_loan_calc * i * 12
        print("YEAR:",i,"BALANCE:", int(result_Remaining_loan_balance),"TOTAL PAYMENT", int(TOTAL_PAYMENT))

# Driver code test
principal = float(input("Please enter the all of loan value : "))
annual_interest_rate = float(input("Please enter the annual interest rate : "))
duration = int(input("Please enter the loan payment duration : "))
Loan_Information(principal, annual_interest_rate, duration)