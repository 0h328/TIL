import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    n = len(height)
    result = 200000
    for i in range(1 << n):
        sum_val = 0
        for j in range(n):
            if i & (1 << j):
                sum_val += height[j]
            if sum_val - B > result:
                break
        if sum_val >= B and sum_val - B < result:
            result = sum_val - B
    print('#{} {}'.format(tc, result))