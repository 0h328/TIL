import sys
sys.stdin = open('input.txt')


def dfs(c, n):
    global res
    if c == K:  # base case
        if int(n) > res:
            res = int(n)
        return

    for i, j in p:
        t = n[:i] + n[j] + n[i + 1:j] + n[i] + n[j + 1:]  # 새로운 숫자 만들기
        if (c, t) not in v:  # 중복 체크(교환 횟수, 숫자)
            v.add((c, t))
            dfs(c + 1, t)


ans = []
T = int(input())
for tc in range(1, T + 1):
    N, K = map(str, input().split())
    K, res = int(K), 0

    v = set()
    p = [(i, j) for i in range(len(N) - 1) for j in range(i + 1, len(N))]  # 교환 가능한 배열

    dfs(0, N)
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')