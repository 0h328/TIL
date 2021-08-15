# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    i = 0
    ans = 0
    # ord(1) = 49, ord(2) = 50, ord(3) = 51
    while i < len(my_str):
        ans += (ord(my_str[-i-1]) - 48) * (10**i)
        i += 1
    return ans


# 문자를 숫자로 변경(while & for 활용)

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int

