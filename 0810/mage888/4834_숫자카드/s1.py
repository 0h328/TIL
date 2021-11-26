import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number = list(map(int, input()))

    cnt = [0] * (max(number)+1)

    for i in range(N):
        cnt[number[i]] += 1

    max_val = 0
    idx_val = 0
    for idx, val in enumerate(cnt):
        if max_val <= val:
            idx_val, max_val = idx, val

    print('#{} {} {}'.format(tc, idx_val, max_val))