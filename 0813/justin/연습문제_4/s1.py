# atoi (ASCII to Integer)
# 문자 -> 숫자 / Python의 int()

# while
def atoi_while(my_str):
    value = 0       # 최종적으로 변환하게 될 숫자
    i = 0           # 문자열에 접근하기 위한 인덱스

    while i < len(my_str):
        char = my_str[i]                        # 문자에서 0번째 값부터 꺼내와서
        if ord('0') <= ord(char) <= ord('9'):   # 0과 9 사이에 있는 값? -> 한 자릿수
            digit = ord(char) - ord('0')        # 자릿수 생성 ==> ord('0') -> 48 / ord('1') -> 49
        else:
            break

        """
        1. 1이 digit으로 들어오는 시점에 value는 초깃값은 0 -> (0 * 10) + 1 이기 때문에 value는 1  
        2. 다음 digit은 2 -> 기존 value가 1 -> (1 * 10) + 2 -> 12
        3. 마지막은 digit이 3 -> value는 12 -> (12 * 10) + 3 -> 123 

        즉, 자릿수가 첫 digit을 시작으로 하나씩 늘어나며 숫자가 뒤에 붙어가는 형태
        """
        value = (value * 10) + digit
        i += 1     # 다음 자리를 확인하자
    return value

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int

# for
def atoi_for(num_str):
    value = 0                       # 최종적으로 변환하게 될 숫자
    for i in range(len(num_str)):
        value *= 10                 # 현재값 * 10
        """
        55 - 48 -> 7
        56 - 48 -> 8
        57 - 48 -> 9
        과 같은 방식으로 해당 자릿수의 숫자를 얻을 수 있음 
        """
        char = num_str[i]
        value += ord(char) - ord('0')
    return value

my_str = atoi_for(my_str)
print(my_str, type(my_str)) # 123, int
