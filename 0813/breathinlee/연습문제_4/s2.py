# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    ans = 0
    l = len(num_str)
    for i in range(l):
        ascii_num = ord(num_str[l-i-1]) - 48
        ans += ascii_num * (10**i)
    return ans

# 문자를 숫자로 변경(while & for 활용)

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int