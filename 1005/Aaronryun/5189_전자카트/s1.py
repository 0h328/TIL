import sys

sys.stdin = open('input.txt')


def dfs(x, total):
    global answer

    if 0 not in visited: # 모두 방문한 경우
        total += data[x][0] # 마지막 돌아온 곳 더해주고
        if total < answer: # 최솟값 갱신
            answer = total
            return
    if total > answer: # 중간에 최소값보다 커지는 경우 볼 필요 없음 가지치기
        return
    for i in range(N):
        if not data[x][i]: # 만약 더할 연료 없다면 그냥 지나감
            continue
        if not visited[i]: # 방문안한 곳이면
            visited[i] = 1
            dfs(i, total + data[x][i]) # 그 위치 연료만큼 더해주고 다음으로 넘김
            visited[i] = 0

for test in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    visited[0] = 1 # 첫 지점 표시
    answer = 1e9
    dfs(0, 0)
    print('#{} {}'.format(test, answer))
