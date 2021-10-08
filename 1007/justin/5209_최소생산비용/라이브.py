import sys

sys.stdin = open('input_5209.txt', 'r')


# idx : 제품번호
# s : 중간 계산 결과
def factory(idx, s):
    global ans
    # 모든 공장에 제품을 결정을 했당
    if idx == N:
        if s < ans:
            ans = s
    elif s >= ans:
        return
    else:
        for i in range(N):  # 공장을 고르자!!
            if visited[i] == 0:
                visited[i] = 1
                factory(idx + 1, s + cost[idx][i])  # 이번 제품 비용을 추가해서 내려보내자~~!
                visited[i] = 0


# idx : 제품번호
# s : 중간 계산 결과
# visit: 정수
def factory2(idx, s, visit):
    global ans
    # 모든 공장에 제품을 결정을 했당
    if visit == (1 << N) - 1:
        if s < ans:
            ans = s
    elif s >= ans:
        return
    else:
        for j in range(N):  # 공장을 고르자!!
            if visit & (1 << j): continue
            factory2(idx + 1, s + cost[idx][j], visit | (1 << j))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())  # 제품 수 이자, 공장 수 3 <= N <= 15
    cost = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321

    visited = [0] * N  # 해당 공장 쳌 위함.

    # factory(0, 0)

    factory2(0, 0, 0)

    print("#{} {}".format(tc, ans))
