import sys
sys.stdin = open('input.txt')


def perm(n, k, m):
    if n == k:
        a = set()
        for i in range(k):
            a.add(nums[i])
        if a not in b:
            b.append(a)
    else:

        for i in range(n, m):
            nums[n], nums[i] = nums[i], nums[n]
            perm(n+1, k, m)
            nums[n], nums[i] = nums[i], nums[n]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1]
    dc = [1, 0]
    nums = [i for i in range((2 * N-1)-1)]
    b = []
    perm(0, N-1, 2*(N-1))
    ans = 987654321
    for c in b:
        seq = [0] * 2 * (N - 1)
        for d in c:
            seq[d] = 1
        total = 0
        y = 0
        x = 0
        s = 0
        total += arr[y][x]
        while True:
            y += dr[seq[s]]
            x += dc[seq[s]]
            total += arr[y][x]
            s += 1
            if s == 2*(N-1):
                s = 0
                break
        if ans > total:
            ans = total
    print('#{} {}'.format(test_case, ans))
