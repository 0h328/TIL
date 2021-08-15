# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    n = len(num_str)
    negative = 1
    result = 0
    for i in range(n):
        if num_str[i] == '-':
            negative = -1
            continue
        if num_str[i] >= '0' and num_str <= '9':
            digit = int(num_str[i])
            result = result * 10 + digit
        else:
            break

    return result * negative

my_str = '-123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int