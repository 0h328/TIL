import sys
sys.stdin = open('input.txt')

def solve(N, M, cnt):
    global ans
    if cnt > ans:
        ans = cnt
        return

    if N == M:
        return
    elif N == (M+1):
        M += 1
        return cnt
    elif N == (M-1):
        M -= 1
        return cnt
    else:
        if M%2:
            solve(N, (M+1)//2, cnt+2)
            solve(N, (M-1)//2, cnt+2)
        else:
            solve(N, M//2, cnt)




T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = 0
    cnt = solve(N, M, 0)
