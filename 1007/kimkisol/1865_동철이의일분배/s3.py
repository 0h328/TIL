import sys
# 4.94915s
sys.stdin = open('input.txt')


def find_max_probability(idx, temp_p, lst_p):
    global max_p

    if idx == N:
        if temp_p > max_p:
            max_p = temp_p
            max_p_list.append(lst_p)
            print(max_p)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_max_probability(idx + 1, temp_p * p[idx][i], lst_p + [i])
            visited[i] = 0

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    p = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_p_list = []
    max_p = 0
    res = 1

    find_max_probability(0, 1, [])
    print(max_p_list)
    for i in range(N):
        print(p[i][max_p_list[-1][i]])
        res = res * p[i][max_p_list[-1][i]] / 100
    print(res)

    print('#{} {:.6f}'.format(t, res))