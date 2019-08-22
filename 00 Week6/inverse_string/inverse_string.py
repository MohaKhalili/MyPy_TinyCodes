# inverse the string program

def inverse_string(my_str):
    new_str = ""
    for i in range(len(my_str)):
        new_str = new_str + my_str[-1-i]
    return new_str

String = "hello there"
result = inverse_string(String)
print(result)