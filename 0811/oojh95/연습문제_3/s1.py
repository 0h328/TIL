import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))

n = len(arr)

for i in range(1 << n):
    sum_arr = 0
    for j in range(n + 1):
        if i & (1 << j):
            print(arr[j], end=' ')
            sum_arr += arr[j]
    if sum_arr == 10:
        print('vvvvvv')
    else:
        print()