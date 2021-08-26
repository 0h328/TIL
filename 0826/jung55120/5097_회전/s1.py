import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    cnt = 0
    while cnt <= M:
        data.append(data.pop(0))
        cnt += 1

    print('#{} {}'.format(tc, data[-1]))