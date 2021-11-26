from pprint import pprint
import sys
sys.stdin = open('input.txt')


# thought process:  10 분
# 코드들을 불러온다
# 16진수들을 2진수로 변환한다 (16 >> 10 >> 2진수 순으로 변환)
# 2진수들을 주어진 암호 해독 비율과 대조하여 10진수로 바꾼다
# 유효한 암호인지 판별한다
# 유효하면 해당 숫자들의 합을 반환
# 아니면 0 을 반환
int(input())
for tc in range(1, 2):

    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    nice = list(set(arr))
    pprint(nice)

    binary = []
    for i in nice:
        # j = i.strip('0')
        # print(j)
        tmp = int(i, 16)
        print(tmp)
        if tmp:
            binary.append(bin(tmp))
    print(binary)
    print()
    print('---------------------------------------------------------------------')
    print()
