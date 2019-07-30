def find_integer_with_most_divisors(input_list):
    def max_num_in_list( list ):
        max = list[ 0 ]
        for a in list:
           if a > max:
               max = a
        return list.index(max)
    CountList = []
    for i in input_list:
        count = 0
        Divisor = 1
        while Divisor <= i:
            if i % Divisor == 0:
                count = count + 1
            Divisor = Divisor + 1
        CountList.append(count)
    x = max_num_in_list(CountList) 
    return input_list[x]
r =  [8, 12, 18, 6]
ty = find_integer_with_most_divisors(r)
print(ty)