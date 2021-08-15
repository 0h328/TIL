# atoi (ASCII to Integer) - while


def atoi_while(my_str):

    idx = len(my_str)-1
    digit = 1
    changed = 0

    while idx >= 0:
        changed += (ord(my_str[idx]) - ord('0')) * digit
        digit *= 10
        idx -= 1

    return changed


my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int

# atoi (ASCII to Integer) - for


def atoi_for(num_str):

    changed = 0

    for e in num_str:
        digit = 10 ** (len(num_str) - 1 - num_str.index(e))
        changed += (ord(e) - ord('0')) * digit

    return changed


my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int