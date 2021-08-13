# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    result = 0
    for num in num_str:
        result = result * 10 + ord(num) - ord('0')
    return result


my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int