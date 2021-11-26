# encoding='UTF8'을 넣지 않으면 계속 UnicodeDecodeError 가 발생하는데 왜그러는지 몰르겠다.
# 해결하느라 30분이 날라갔다.

import sys
sys.stdin = open('input.txt', encoding='UTF8')

def pattern_count(target, pattern, N, M):
    cnt = 0
    for i in range(0, N - M + 1):
        my_str = ''
        for j in range(i, i + M):
            my_str += target[j]
        if my_str == pattern:
            cnt += 1
    return cnt

for _ in range(10):
    T = int(input())
    pattern = input()
    target = input()
    M = len(pattern)
    N = len(target)

    ans = pattern_count(target, pattern, N, M)
    print('#{} {}'.format(T, ans))
