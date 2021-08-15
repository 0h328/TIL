# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    i = 0
    result = 0
    if my_str[i] == '-':
        negative = -1
        i +=1
    else:
        negative = 1
    while i < len(my_str):
        if my_str[i] >= '0' and my_str[i] <= '9':
            digit = int(my_str[i]) - 0
        else:
            break
        result = (result * 10) + digit
        i += 1
    return result * negative

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int

