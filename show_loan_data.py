#####################################################################################################################
# Your function for calculating payment goes here
def Mounthly_payment(principal, annual_interest_rate, duration):
    n = duration * 12
    if annual_interest_rate != 0:
        r = (annual_interest_rate / 100) / 12
        Mounthly_payment = (principal * (r * ((1+r)**n))) / (((1+r)**n) - 1)
    else:
        Mounthly_payment = principal / n
    return Mounthly_payment


# Your function for calculating remaining balance goes here
def Remaining_loan_balance(principal,annual_interest_rate,duration,number_of_payments):
    n = duration * 12
    p = number_of_payments
    if annual_interest_rate != 0:
        r = (annual_interest_rate / 100) / 12
        Remaining_loan_balance = (principal * ( ((1+r)**n) - ((1+r)**p) )) / (((1+r)**n) - 1)
    else:
        Remaining_loan_balance = principal * (1- (p/n))
    return Remaining_loan_balance         



# Your main program goes here
principal=float(input("Enter loan amount: "))
annual_interest_rate=float(input("Enter annual interest rate (percent): "))
duration=int(input("Enter loan duration in years: "))

print("LOAN AMOUNT:",int(principal),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
print("DURATION (YEARS):",duration,"MONTHLY PAYMENT:",int(Mounthly_payment(principal,annual_interest_rate,duration)))

for i in range(1,duration+1):
    BALANCE = Remaining_loan_balance(principal,annual_interest_rate,duration,i*12)
    TOTAL_PAYMENT = i*12*Mounthly_payment(principal,annual_interest_rate,duration)
    print("YEAR:",i,"BALANCE:",int(BALANCE),"TOTAL PAYMENT",int(TOTAL_PAYMENT))



#####################################################################################################################
