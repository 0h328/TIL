import sys

sys.stdin = open('input.txt')


def dfs(node, ans):
    global answer

    if node >= 12:
        if answer > ans:
            answer = ans
        return
    elif ans > answer:
        return

    dfs(node + 1, ans + (day * plan[node]))
    dfs(node + 1, ans + month)
    dfs(node + 3, ans + three_month)


T = int(input())

for tc in range(1, T + 1):
    day, month, three_month, year = map(int, input().split())
    plan = list(map(int, input().split()))
    answer = year

    dfs(0, 0)

    print('#{} {}'.format(tc, answer))