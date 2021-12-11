import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def is_queen(x):
    for i in range(x):
        if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
            return 0
    return 1


def dfs(x):
    global res

    if x == N:
        res += 1
    else:
        for i in range(N):
            arr[x] = i
            if is_queen(x):
                dfs(x+1)

N = int(input())
arr = [0] * N
res = 0
dfs(0)
print(res)