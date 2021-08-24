# 인접행렬
# 재귀보단 인접행렬이 낫다.
# 재귀가 간단해보이는데, 이해하는건 인접행렬이 더 쉽다.
# 아무튼 인접행렬이 더 낫다.
# 웹엑스 시간에 배운 코드 그냥 계속 손으로 쓰고 손디버깅 하다보니까 저절로 외워졌다.
# 외워진 코드에 도착지점 확인 여부만 덧붙였다.

import sys
sys.stdin = open('input.txt')

def dfs():
    # global s            # 함수 내 s가 없음.
    stack = [s]
    # stack = [0]

    while stack:
        s = stack.pop()

        if not visited[s]:
            visited[s] = 1

            for w in range(100):
                if G[s][w] == 1 and not visited[w]:
                    stack.append(w)

    if visited[e]:      # 여기에 쓴 이유는 while문을 다 돌았을때 visited에 도착지점이 True면 도착지에 도착했으니까.. 맞나?
        return 1
    else:
        return 0

T = 10
for tc in range(1, T+1):
    N, E = map(int, input().split())
    temp = list(map(int, input().split()))

    G = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(E):
        G[temp[i*2]][temp[i*2+1]] = 1

    visited = [0 for _ in range(100)]

    s = 0       # global
    e = 99

    print('#{} {}'.format(tc, dfs()))




