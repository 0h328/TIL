# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    # my_str.isdigit()

    answer = 0
    i = len(my_str) - 1  # 10의 지수 구함

    for c in my_str:
        ascii_tmp = ord(c) - 48  # 문자 0 의 아스키 코드값 48
        answer += ascii_tmp * (10 ** i)  # 10의 i 제곱을 곱해서 더해줌s
        i -= 1

    return answer

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int