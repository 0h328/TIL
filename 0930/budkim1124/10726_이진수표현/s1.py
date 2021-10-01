import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    s = []
    while M > 0:
        a = M % 2
        s.append(a)
        M = M // 2

    s = s[::-1]
    result = 'OFF'
    if len(s) >= N:
        if all(s[len(s)-N : len(s)]) == 1:
            result = 'ON'

    print('#{} {}'.format(t+1, result))
