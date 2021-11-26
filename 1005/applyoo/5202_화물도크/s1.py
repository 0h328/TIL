import sys
sys.stdin = open('input.txt')


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = sorted(list(tuple(map(int, input().split())) for _ in range(N)), key=lambda x: x[1], reverse=True)

    res, cur = 1, arr.pop()[1]
    while arr:
        s, e = arr.pop()

        if cur <= s:
            res += 1
            cur = e

    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
