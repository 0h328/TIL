import sys

sys.stdin = open('input.txt')

T = int(input())


def find(a):
    global ans, temp_ans
    if temp_ans >= ans:
        return
    if a != N:
        for k in range(N):
            if k in list_N:
                list_N.remove(k)
                temp_ans += cost[a][k]
                find(a + 1)
                list_N.append(k)
                temp_ans -= cost[a][k]
    if a == N:
        if ans > temp_ans:
            ans = temp_ans


for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    list_N = list(range(N))
    ans = 50000
    temp_ans = 0
    find(0)
    print('#{} {}'.format(tc, ans))
