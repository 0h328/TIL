import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    max_val = data[0]
    min_val = data[0]

    for i in range(1, len(data)):
        if max_val < data[i]:
            max_val = data[i]
            continue
        if min_val > data[i]:
            min_val = data[i]

    ans = max_val - min_val
    print('#{} {}'.format(tc, ans))