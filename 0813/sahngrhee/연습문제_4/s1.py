# atoid (ASCII to Integer) - while

def atoi_while(my_str):
    my_num = 0
    for i in range(len(my_str)):
        my_num += (ord(my_str[i])-48) * (10 ** (len(my_str)-(i+1)))

    return my_num

my_str = '123'
print(my_str, type(my_str)) # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int