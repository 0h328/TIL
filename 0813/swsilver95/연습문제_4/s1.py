# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    i = 0
    result = 0
    while i < len(my_str):
        a = ord(my_str[i]) - ord('0')
        result = result * 10 + a
        i += 1
    return result

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int