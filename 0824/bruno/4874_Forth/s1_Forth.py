import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    my_string = list(input().split())
    my_string.pop()     # .제거
    result = []

    cnt_operator = 0    # 연산자 갯수
    cnt_operand = 0     # 피연산자 갯수

    for strs in my_string:      # 연산자와 피연산자 갯수를 세어보자
        if strs in ['+', '-', '*', '/']:
            cnt_operator += 1
        else:
            cnt_operand += 1

    if cnt_operand != (cnt_operator + 1):   # 피연산자 갯수 = 연산자 갯수 + 1 인지 확인
        print('#{} {}'.format(tc, 'error')) # 아니라면 에러반환하고
        continue                            # 아래는 수행하지 않고 반복문 종료
    else:
        for strs2 in my_string:

            if strs2 == '+':
                b = result.pop()
                a = result.pop()
                c = int(a) + int(b)
                result.append(c)
            elif strs2 == '-':
                b = result.pop()
                a = result.pop()
                c = int(a) - int(b)
                result.append(c)
            elif strs2 == '*':
                b = result.pop()
                a = result.pop()
                c = int(a) * int(b)
                result.append(c)
            elif strs2 == '/':
                b = result.pop()
                a = result.pop()
                c = int(a) // int(b)
                result.append(c)
            else:
                result.append(int(strs2))

    print('#{} {}'.format(tc, result[0]))