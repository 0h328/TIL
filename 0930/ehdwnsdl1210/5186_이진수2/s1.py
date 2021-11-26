'''
0보다 크고 1미만인 십진수 N을 이진수로 바꾸려고 한다. 예를 들어 0.625를 이진 수로 바꾸면 0.101이 된다.
N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
13자리 이상이 필요한 경우에는 ‘overflow’를 출력하는 프로그램을 작성하시오.
'''


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    # print(N)
    result = ''
    while N * 2 - 1 != 0:                               # 0.625 -> 1.25(-1) -> 0.25 -> 0.5(0) -> 1(끝나버림)
        if N * 2 >= 1:
            result += '1'
            N = N * 2 - 1
        else:
            result += '0'
            N = N * 2
    result += '1'                                       # 1추가(보정해줘야)

    # print('#{} {}'.format(tc, result))

    if len(result) > 12:
        print('#{} {}'.format(tc, 'overflow'))          # 이게 왜 되지 (최소로 표현?) / 0001100110011001100110011001100110011001100110011001101
    else:
        print('#{} {}'.format(tc, result))