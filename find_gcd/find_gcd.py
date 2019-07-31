# GCD of more than two (or array) numbers 
# Function implements the Euclidian
def Find_GCD(my_list):     
    
    def Find_GCD_TwoNum(x, y): 
        while(y): 
            x, y = y, x % y 
        return x 
  
    num1 = my_list[0] 
    num2 = my_list[1] 
    gcd = Find_GCD_TwoNum(num1, num2) 
  
    for i in range(2, len(my_list)): 
        gcd = Find_GCD_TwoNum(gcd, my_list[i])
    return gcd
# driver code for test the GCD finder function
List = [3, 5, 9, 11, 13]
e = Find_GCD(List)
print(e)