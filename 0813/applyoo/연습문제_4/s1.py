# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    result = 0
    idx = len(my_str) - 1
    while idx > -1:
        result += int(my_str[idx]) * (10**(len(my_str)-idx-1))
        idx -= 1
    return result

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int

# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    result = 0
    for i in range(len(num_str)-1, -1, -1):
        result += int(my_str[i]) * (10 ** i)
    return result

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int