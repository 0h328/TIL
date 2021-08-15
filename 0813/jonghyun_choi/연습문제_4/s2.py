# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    pos = len(num_str) - 1
    total = 0
    for i in num_str:
        total += (ord(i) - 48) * (10**pos)
        pos -= 1
    return total



my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int