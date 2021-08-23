import sys
sys.stdin = open('input.txt')

# 전체길이 - (패턴횟수 * 길이) + 패턴횟수 7 - (2 * 2) + 2

# text에서 pattern이 존재 가능한 모든 시작 위치

T = int(input())

for tc in range(1, T+1):
    t, p = input().split()
    n, m = len(t), len(p)
    cnt = 0
    i = 0

    while i < n - m + 1:
        for j in range(m):
            if p[j] != t[i+j]:
                break
        else:
            cnt += 1
            i = i + m -1
        i += 1

    print('#{} {}'.format(tc, n - (cnt * m) + cnt))