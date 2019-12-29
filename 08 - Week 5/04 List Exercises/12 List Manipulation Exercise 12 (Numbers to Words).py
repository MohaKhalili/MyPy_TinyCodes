# A program that asks the user to enter an integer between 1 and 9999 
# (both inclusive) and then prints the input integer using words. For 
# example if the user enters : 3421

# Then your program should print : 
# three thousand four hundred twenty one


# Type your code here
n=int(input('please enter an integer between 1 and 9999: '))

numbers_1to19 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
                'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 
                'seventeen', 'eighteen', 'nineteen']
numbers_dahgan_10to90 = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

num_digit = len(str(n))

if num_digit == 1:
    print(numbers_1to19[n-1])

elif num_digit == 2:
    if n < 20:
        print(numbers_1to19[n - 1])
    elif n % 10 == 0:
        dahgan = n // 10
        print(numbers_dahgan_10to90[dahgan-1])
    elif n % 10 != 0:
        dahgan = n // 10
        yekan = n - (dahgan*10)
        print(numbers_dahgan_10to90[dahgan-1],numbers_1to19[yekan - 1])

elif num_digit == 3:
    if n % 100 == 0:
        sadgan = n // 100
        print(numbers_1to19[sadgan-1],'hundred')
    elif n % 10 == 0:
        sadgan = n // 100
        dahgan = (n - (sadgan*100)) // 10
        print(numbers_1to19[sadgan-1],'hundred',numbers_dahgan_10to90[dahgan-1])
    else:
        sadgan = n // 100
        dahgan = n - (sadgan*100)
        if dahgan < 20:
            print(numbers_1to19[sadgan-1],'hundred',numbers_1to19[dahgan-1])
        else:
            dahgan = (n-(sadgan*100)) // 10
            yekan = n - (sadgan*100) - (dahgan*10)
            print(numbers_1to19[sadgan-1],'hundred',numbers_dahgan_10to90[dahgan-1],numbers_1to19[yekan-1])

elif num_digit == 4:
    if n % 1000 == 0:
        hezaregan = n // 1000
        print(numbers_1to19[hezaregan - 1], 'thousand')
    elif n % 100 == 0:
        hezaregan = n // 1000
        sadgan = (n - (hezaregan*1000)) // 100
        print(numbers_1to19[hezaregan-1], 'thousand', numbers_1to19[sadgan-1],'hundred')
    elif n % 10 == 0:
        hezaregan = n // 1000
        number = n - (hezaregan*1000)
        if number > 100:
            sadgan = (n - (hezaregan*1000)) // 100
            dahgan = (n - (hezaregan*1000) - (sadgan*100)) // 10
            print(numbers_1to19[hezaregan-1], 'thousand',numbers_1to19[sadgan-1], 'hundred', numbers_dahgan_10to90[dahgan-1])
        else:
            dahgan = (n - (hezaregan*1000)) // 10
            print(numbers_1to19[hezaregan-1], 'thousand', numbers_dahgan_10to90[dahgan-1])
    else:
        hezaregan = n // 1000
        number = n - (hezaregan*1000)
        if number < 20:
            print(numbers_1to19[hezaregan-1], 'thousand',numbers_1to19[number-1])
        elif (number < 100) and (number % 10 != 0):
            dahgan = (n - (hezaregan*1000)) // 10
            yekan = n - (hezaregan*1000) - (dahgan*10)
            print(numbers_1to19[hezaregan-1], 'thousand', numbers_dahgan_10to90[dahgan-1], numbers_1to19[yekan-1])
        elif (number // 100 >= 1):
            if (number % 100 < 20):
                print(numbers_1to19[hezaregan-1], 'thousand', numbers_1to19[(number//100)-1], 'hundred', numbers_1to19[(number%100)-1])
            else:
                sadgan = (n - (hezaregan*1000)) // 100
                dahgan = (n - (hezaregan*1000) - (sadgan*100)) // 10
                yekan = n - (hezaregan*1000) - (sadgan*100) - (dahgan*10)
                print(numbers_1to19[hezaregan-1], 'thousand', numbers_1to19[sadgan-1], 'hundred',numbers_dahgan_10to90[dahgan-1],numbers_1to19[yekan-1])


################### Instructor code ###################
n=int(input('please enter an integer between 1 and 9999: '))
one_to_ten=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_to_nineteen=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_to_ninety=['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety']
temp_str=""
if n==0:
    temp_str='zero'
    #print('zero')
first_digit=n//1000
second_digit=(n%1000)//100
third_digit=(n%100)//10
fourth_digit=(n%10)
if first_digit>0:
    temp_str=temp_str+one_to_ten[first_digit]+' thousand '
    #print (one_to_ten[first_digit],'thousand ',end='')
if second_digit>0:
    temp_str=temp_str+one_to_ten[second_digit]+' hundred '
    #print (one_to_ten[second_digit],'hundred ',end='')
if third_digit>1:
    temp_str=temp_str+twenty_to_ninety[third_digit]+" "
    #print (twenty_to_ninety[third_digit],'',end='')
if third_digit==1:
    temp_str=temp_str+ten_to_nineteen[fourth_digit]+" "
    #print (ten_to_nineteen[fourth_digit],'',end='')
else:
    if fourth_digit:
        temp_str=temp_str+one_to_ten[fourth_digit]+" "
        #print (one_to_ten[fourth_digit],'',end='')
if temp_str[-1]==" ":
    temp_str=temp_str[0:-1]
print (temp_str)