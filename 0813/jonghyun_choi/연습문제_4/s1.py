# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    i = 0
    total = 0
    j = len(my_str)-1
    while i < len(my_str):
        total += (ord(my_str[i]) - 48) * (10**j)
        j -= 1
        i += 1
    return total


my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int