import sys

sys.stdin = open('input.txt')

# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    result = 0
    i=0
    while i<len(my_str):
        result += (ord(my_str[i]) - ord('0')) * (10 ** (len(my_str) - 1 - i))
        i+=1
    return result

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int