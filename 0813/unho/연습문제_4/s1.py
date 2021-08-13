# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    # my_str.isdigit()

    answer = 0
    i = 0

    while i < len(my_str):
        ascii_tmp = ord(my_str[-i-1]) - 48      # 뒤에 문자부터
        answer += ascii_tmp * (10**i)
        i += 1

    return answer

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int