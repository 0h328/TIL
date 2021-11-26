import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    max_val = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if box[i] <= box[j]:
                cnt += 1
        drop = N - i - 1 - cnt
        if max_val < drop:
            max_val = drop
    print('#{} {}'.format(tc, max_val))