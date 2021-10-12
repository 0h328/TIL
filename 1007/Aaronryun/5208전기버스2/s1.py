import sys

sys.stdin = open('input.txt')


def dfs(idx, total):
    global answer
    if answer < total: return

    if idx >= N-1: # 정류장을 벗어나면
        answer = total
        return

    now = station[idx]
    for i in range(now, 0, -1): # 최대부터 한칸 씩 줄여가면서
        dfs(idx + i, total + 1)


for test in range(1, 1 + int(input())):
    answer = 1e9
    station = list(map(int, input().split()))

    N = station.pop(0)
    dfs(0, -1)

    print('#{} {}'.format(test, answer))

# def dfs(start,tmp):
#     print(tmp, start)
#     if battery[start]+start >= station:
#
#         result.append(tmp)
#         return
#     for i in range(1,battery[start]+1):
#         tmp.append(battery[start])
#         dfs(start+i,tmp)
#         tmp.pop()
