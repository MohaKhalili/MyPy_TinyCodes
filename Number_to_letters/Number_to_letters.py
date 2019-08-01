x=int(input('please enter an integer between 1 and 9999: '))

def Number_to_letters(n):
     
    def convert_fun(n):
        if n == 1:
            return 'one'
        elif n == 2:
            return 'two'
        elif n == 3:
            return 'three'
        elif n == 4:
            return 'four'
        elif n == 5:
            return 'five'
        elif n == 6:
            return 'six'
        elif n == 7:
            return 'seven'
        elif n == 8:
            return 'eight'
        elif n == 9:
            return 'nine'
        elif n == 10:
            return 'ten'
        elif n == 11:
            return 'eleven'
        elif n == 12:
            return 'twelve'
        elif n == 13:
            return 'thirteen'
        elif n == 14:
            return 'fourteen'
        elif n == 15:
            return 'fifteen'
        elif n == 16:
            return 'sixteen'
        elif n == 17:
            return 'seventeen'
        elif n == 18:
            return 'eighteen'
        elif n == 19:
            return 'nineteen'
        elif n == 20:
            return 'twenty'
        elif n == 30:
            return 'thirty'
        elif n == 40:
            return 'forty'
        elif n == 50:
            return 'fifty'
        elif n == 60:
            return 'sixty'
        elif n == 70:
            return 'seventy'
        elif n == 80:
            return 'eighty'
        elif n == 90:
            return 'ninety'

    if n >= 1 and n <= 20:
        print(convert_fun(n))
    
    elif n>=21 and n<=99 and (n % 10 == 0):
        print(convert_fun(n))
    
    elif n>=21 and n<=99:
        yekan = n % 10
        dahgan = n - yekan
        print(convert_fun(dahgan),convert_fun(yekan))
    
    elif n>=100 and n<=999 and (n % 100 == 0):
        for i in range(1,10):
            if n // 100 == i:
                print(convert_fun(i),"hundred")
    
    elif n>=100 and n<=999:
        baghiye = n % 100
        if (baghiye < 20) or (baghiye % 10 == 0):
            for i in range(1,10):
                if (n - baghiye) // 100 == i:
                    print(convert_fun(i),"hundred",convert_fun(baghiye))
        elif baghiye > 20 and baghiye % 10 != 0:
            yekan = baghiye % 10
            dahgan = baghiye - yekan
            sadgan = n - baghiye
            for i in range(1,10):
                if sadgan // 100 == i:
                    print(convert_fun(i),"hundred ", end = "")
            print(convert_fun(dahgan),convert_fun(yekan))    

    elif n>=1000 and n<=9999 and (n % 1000 == 0):
        for i in range(1,10):
            if n // 1000 == i:
                print(convert_fun(i),"thousand")

    elif n>=1000 and n<=9999:
        baghiye = n % 1000
        if (baghiye < 20) or (baghiye >= 20 and baghiye < 100 and baghiye % 10 == 0):
            for i in range(1,10):
                if (n - baghiye) // 1000 == i:
                    print(convert_fun(i),"thousand",convert_fun(baghiye))
        elif (baghiye >= 20 and baghiye < 100 and baghiye % 10 != 0):
            yekan = baghiye % 10
            dahgan = baghiye - yekan
            for i in range(1,10):
                if (n - baghiye) // 1000 == i:
                    print(convert_fun(i),"thousand",convert_fun(dahgan),convert_fun(yekan))
        elif (baghiye >= 100 and baghiye < 999 and baghiye % 100 == 0):
            for i in range(1,10):
                if (n - baghiye) // 1000 == i:
                    print(convert_fun(i),"thousand ", end = "")
            for i in range(1,10):
                if baghiye // 100 == i:
                    print(convert_fun(i),"hundred")
        elif (baghiye >= 100 and baghiye < 999 and baghiye % 100 != 0):   
            for i in range(1,10):
                if (n - baghiye) // 1000 == i:
                    print(convert_fun(i),"thousand ", end = "")
            for i in range(1,10):
                if baghiye // 100 == i:
                    print(convert_fun(i),"hundred ", end = "")
            sadgan = baghiye % 100
            if sadgan % 10 == 0 or sadgan < 20:
                print(convert_fun(sadgan))
            else:
                yekan = sadgan % 10
                dahgan = sadgan - yekan
                print(convert_fun(dahgan),convert_fun(yekan))      

Number_to_letters(x)