# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    idx = 0
    result = ''
    while idx < len(my_str):
        result += str(ord(my_str[idx]) - 48)
        idx += 1
    return int(result)

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int

# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    result = ''
    for num in num_str:
        result += str(ord(num) - 48)
    return int(result)

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int