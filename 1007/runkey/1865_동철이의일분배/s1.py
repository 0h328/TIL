import sys
sys.stdin = open('input.txt')

def dfs(idx, max_n):
    global res          # 최종 결과값 글로벌로 받아옴
    if max_n == 0:      # 현재 최대 값이 0이면
        return          # 함수 종료
    if res >= max_n:    # 소수는 곱할수록 작아지므로 중간에 최종 결과값보다 작아지면
        return          # 함수 종료
    if idx == N:        # 현재 인덱스가 N이랑 같아지면
        res = max_n     # 결과값에 현재 최대값 max_n을 넣어줌
        return          # 함수 종료

    for i in range(N):          # N개에 대해 전부 조회
        if not visited[i]:      # 방문하지 않았다면
            visited[i] = 1      # 방문표시
            dfs(idx + 1, max_n * N_list[i][idx])    # 인덱스 하나 늘려주고, 현재 결과값에 현재 확률 곱해줌
            visited[i] = 0      # 모든 경우를 확인해야 하므로 함수 종료 후 방문 취소

tc = int(input())
for t in range(1, tc + 1):
    N = int(input())     # N명의 직원
    N_list = [list(map(int, input().split())) for _ in range(N)]    # 일의 성공확률
    visited = [0] * N   # 방문 여부
    for i in range(N):
        for j in range(N):
            N_list[i][j] /= 100 # 모든 확률 100으로 나눠줌
    res = 0     # 최종 결과값
    max_n = 1   # 현재 최대값
    idx = 0     # 현재 인덱스
    dfs(idx, max_n)     # dfs 함수
    res *= 100  # 함수 다 돌고 나온 최종 결과값에 100 곱해줌
    print("#{} {:.6f}".format(t, res))