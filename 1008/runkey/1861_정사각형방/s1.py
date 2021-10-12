import sys
sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc + 1):
    print("#{}".format(t), end=" ")
    N = int(input())
    N_list = [[0] for _ in range(N)]
    for k in range(N):
        N_list[k] = list(map(int, input().split()))

    visited = [0] * (N * N + 1)
    # 상하 좌우 탐색하면서 차이가 -1인 곳을 탐색
    for i in range(N):
        for j in range(N):
            if (i != 0 and N_list[i][j] - N_list[i - 1][j] == -1) or \
                (i != N - 1 and N_list[i][j] - N_list[i + 1][j] == -1) or \
                (j != 0 and N_list[i][j] - N_list[i][j - 1] == -1) or \
                (j != N - 1 and N_list[i][j] - N_list[i][j + 1] == -1):
                visited[N_list[i][j]] = 1   # visited 인덱스를 숫자로 넣어줌

    # 가장 작은 수를 찾아야 하므로 역탐색
    for k in range(N * N - 2 , -1, -1):
        if visited[k] == 1: # 경로가 존재할 시
            visited[k] += visited[k + 1]    # 다음 숫자 visited + 1

    print(visited.index(max(visited)), max(visited) + 1)    # 최댓값의 인덱스(가장 작은 수), 큰 수 + 1 (자신 포함) 출력