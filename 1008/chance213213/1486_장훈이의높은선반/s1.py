import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    height_arr = []
    for i in range(1, 2**N):
        new_arr = []
        for j in range(N):
            if i & (1 << j):
                new_arr.append(1)
            else:
                new_arr.append(0)
        height = 0
        for idx in range(len(new_arr)):
            height += new_arr[idx]*S[idx]
        height_arr.append(height)

    height_arr.sort()
    for num in height_arr:
        if num >= B:
            ans = num
            break

    print('#{} {}'.format(tc, ans-B))