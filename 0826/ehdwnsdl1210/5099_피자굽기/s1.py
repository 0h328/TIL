import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # N : 화덕 크기 / M : 피자 개수

    Ci = list(map(int, input().split()))
    Ci_c = Ci[:]
    visited = [0] * (M+1)
    hwa = [0]
    result = 0

    for _ in range(N):
        hwa.append(Ci.pop(0))
        visited[N+1] += 1

    while hwa.count(0) < N - 1:
        for i in range(1, len(hwa)):
            if hwa[i] // 2 > 0:
                hwa[i] = i // 2
            else:
                hwa[i] = 0
                if len(Ci) > 0:
                    hwa[i] = Ci.pop(0)
                    visited[M-len(Ci)+1] += 1
    for j in hwa:
        if j != 0:
            result = Ci_c.index(j)

    print('#{} {}'.format(tc, result))
# index 담을 그릇!
'''
#1 4
#2 8
#3 6
'''