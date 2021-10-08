import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(number, change, battery):
    global ans
    if change >= ans:
        return

    if number + M[number] >= N - 1:
        ans = change
        return

    for i in range(battery, 0, -1):
        dfs(number + i, change + 1, M[number + i])


for case in range(T):
    data = list(map(int, input().split()))
    N = data[0]
    M = data[1:]
    ans = 987654321
    dfs(0, 0, M[0])

    print('#{} {}'.format(case + 1, ans))