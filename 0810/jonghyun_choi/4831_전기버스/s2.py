import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    K, N, M = map(int, input().split())
    data = list(map(int, input().split()))
    pos = 0
    cnt = 0
    while pos < N:
        for i in range(K, 0, -1):
            if pos + i >= N:
                pos += i
                break
            if pos + i in data:
                pos += i
                cnt += 1
                break
        else:
            cnt = -1
            break

        if cnt == -1:
            break

    if cnt == -1:
        print('#{} {}'.format(case + 1, 0))
    else:
        print('#{} {}'.format(case + 1, cnt))

