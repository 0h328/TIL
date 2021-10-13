import sys
sys.stdin = open('input.txt')


def path(point, remain):
    global result
    for possible in adj_list[point]:
        if possible not in remain:
            path(possible, remain+[possible])
    else:
        result.append(len(remain))


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        adj_list[x].append(y)
        adj_list[y].append(x)
    ans = 0
    result = []

    for i in range(1, N+1):
        path(i, [i])
        if ans < max(result):
            ans = max(result)

    print('#{} {}'.format(test_case, ans))




