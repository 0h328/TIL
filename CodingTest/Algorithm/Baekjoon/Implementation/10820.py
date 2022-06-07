import sys
sys.stdin = open('input.txt')

while True:
    s = sys.stdin.readline().rstrip('\n')

    lower_cnt = 0
    upper_cnt = 0
    number_cnt = 0
    blank_cnt = 0

    if not s:
        break
    for i in s:
        if i.islower():     # 소문자
            lower_cnt += 1
        elif i.isupper():   # 대문자
            upper_cnt += 1
        elif i.isdigit():   # 숫자
            number_cnt += 1
        elif i.isspace():   # 공백
            blank_cnt += 1

    print(lower_cnt, upper_cnt, number_cnt, blank_cnt)
