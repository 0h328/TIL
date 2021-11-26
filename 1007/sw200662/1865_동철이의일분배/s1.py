import sys

sys.stdin = open('input.txt')

T = int(input())


def find(a):
    global ans, temp_ans
    if temp_ans < ans:
        return
    if a != N:
        for k in range(N):
            if k in list_N and cost[a][k] != 0:
                list_N.remove(k)
                temp_ans *= cost[a][k]
                find(a + 1)
                list_N.append(k)
                temp_ans /= cost[a][k]
    if a == N:
        if ans < temp_ans:
            ans = temp_ans


for tc in range(1, T + 1):
    N = int(input())
    cost = [list(map(float, input().split())) for _ in range(N)]
    for i in range(len(cost)):
        for k in range(len(cost)):
            cost[i][k] /= 100

    list_N = list(range(N))
    ans = 0
    temp_ans = 1
    find(0)
    ans = ans * 100
    print('#{} {:.6f}'.format(tc, ans))
