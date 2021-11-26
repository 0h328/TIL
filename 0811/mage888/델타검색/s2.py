import sys
sys.stdin = open('input2.txt')

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]

    rc = [[0, -1], [1, 0], [0, 1], [-1, 0]]

    ans = 0
    for r in range(n):
        for c in range(n):
            for dr, dc in rc:
                if r+dr in range(n) and c+dc in range(n):
                    ans += abs(a[r][c] - a[r+dr][c+dc])

    print('#{} {}'.format(test_case, ans))