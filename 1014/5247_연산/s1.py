import sys
sys.stdin = open('input.txt')

def solve(N, M):
    global cnt
    if M == N:
        return cnt
    if (M+1) == N:
        M += 1
        cnt += 1
        return cnt
    if (M-1) == N:
        M -= 1
        cnt += 1
        return cnt
    if M % 2:
        for i in range(2):
            M += i
            cnt += 1
            solve(N, M)
            if N == M:
                return cnt

    else:
        M //= 2
        cnt += 1
        solve(N, M)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cnt = 0
    ans = solve(N, M)
    print(ans)

