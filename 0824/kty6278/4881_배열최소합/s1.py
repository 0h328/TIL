import sys
sys.stdin = open('input.txt')

def solve(row):
    global part_sum, min_v
    if part_sum > min_v: # 가지치기
        return

    if row == N: # 마지막 행에 도착한 경우
        min_v = min(part_sum, min_v)  # 최솟값으로 교환

    for i in range(N):               # 행은 동일하게 열을 모두 읽어냄
        if visited[i] == 0:     # 방문하지 않은 경우
            visited[i] = 1     # 방문체크
            part_sum += word[row][i] # 현재 위치 부분합에 추가
            solve(row + 1)           # 아래, 다음행 다시 함수 시작   # part_sum = 2+8+2, min_v = 14
                                                                   # part_sum = 0 > 2+5+2 min_v = 9
            visited[i] = 0      # 방문 x
            part_sum -= word[row][i]  # 부분합에 추가한 것 제외

for tc in range(int(input())):
    N = int(input())
    word = [list(map(int, input().split())) for _ in range(N)]
    # print(word)
    visited = [0] * N
    part_sum = 0
    min_v = 9999999
    solve(0)
    print('#{} {}'.format(tc+1, min_v))

