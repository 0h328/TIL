import sys
sys.stdin = open('input.txt')


def dfs(n, cnt):
    global min_cnt

    if cnt >= min_cnt:
        return
    for i in range(arr[n], 0, -1):
        w = n + i
        if w < N:
            dfs(w, cnt+1)
        else:
            if cnt < min_cnt:
                min_cnt = cnt
            return


T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]

    min_cnt = 100000000000000000
    dfs(1, 0)
    print('#{} {}'.format(tc, min_cnt))
