import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

r = 1                                   # 행 좌표값
c = 1                                   # 열 좌표값

dr = [-1, 1, 0, 0]                      # 상하좌우 구하기 위해서 만들어준 임의의 좌표
dc = [0, 0, -1, 1]

for i in range(4):                      # 상하좌우 4가지를 출력하기 위해 4번 반복
    nr = r + dr[i]                      # 인덱스 i가 들어가면서 r, c 값이 nr, nc로 변경
    nc = c + dc[i]

    if (0 <= nr < N) and (0 <= nc < N): # nc, nr값이 배열에서 넘어가지 않는다면 data에서 좌표에 위치한 숫자들 출력
        print(data[nr][nc])

    if nr < 0 or nr >= N or nc < 0 or nc >= N: # 혹시나 배열에서 nc, nr의 좌표값이 기준을 넘어간다면 아무 것도 하지 않고 넘어가기
        continue
