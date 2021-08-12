import sys

sys.stdin = open('input.txt')

T = int(input())
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(num_list)

idx = 1
while idx <= T:
    N, K = map(int, input().split())

    ans = 0
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(num_list[j])

        if len(subset) == N and sum(subset) == K:
            ans += 1

    print('#{0} {1}'.format(idx, ans))

    idx += 1
