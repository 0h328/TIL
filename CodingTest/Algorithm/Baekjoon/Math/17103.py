import sys
sys.stdin = open('input.txt')

T = int(input())
arr = [0] * T
max_num = 0
for i in range(T):
    N = int(sys.stdin.readline())
    arr[i] = N

    if max_num < N:
        max_num = N

arr_2 = [True] * (max_num + 1)
arr_2[1] = False

for i in range(2, int(max_num ** 0.5) + 1):
    if arr_2[i]:
        for j in range(i + i, max_num + 1, i):
            arr_2[j] = False

for i in arr:
    cnt = 0
    for j in range(2, i // 2 + 1):
        if arr_2[j] and arr_2[i - j]:
            cnt += 1

    print(cnt)
