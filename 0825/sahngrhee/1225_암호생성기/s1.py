'''
1시간 30분이 넘는 시간의 디버깅과 노가다로 결국 답을 찾아냈다.
'''
import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    T = int(input())
    P = list(map(int, input().split()))

    n = 0
    while P[-1] > 0:
        P.append(P.pop(0) - ((n % 5) + 1))
        n += 1

    if P[-1] <= 0:
        P[-1] = 0

    print('#{}'.format(test_case), end=' ')
    print(*P)



