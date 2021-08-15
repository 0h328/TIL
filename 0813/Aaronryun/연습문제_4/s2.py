# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    result = 0
    for i in range(len(num_str)):
        result += (ord(num_str[i])-ord('0'))*(10**(len(num_str)-1-i))
    return result
my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int