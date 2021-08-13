# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    length = len(my_str)
    idx = 0
    ans = 0

    while idx < length:
        ans += int(my_str[idx]) * (10 ** (length - idx - 1))
        idx += 1

    return ans

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int

# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    length = len(num_str)
    ans = 0

    for i in range(length):
        ans += int(num_str[i]) * (10 ** (length - i - 1))

    return ans

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int