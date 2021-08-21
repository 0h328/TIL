# 스택 안 쓰는 풀이

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    iron_bar = input()

    cnt = 0
    ans = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if iron_bar[i-1] == '(':
                ans += cnt
            else:
                ans += 1

    print('#{} {}'.format(tc, ans))