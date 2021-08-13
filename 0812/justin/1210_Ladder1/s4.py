def solve(goal):
    """
    도착지부터 사다리 위로 올라가는 함수
    :param goal: 시작지점
    :return:     출발지점
    """
    i = 99                                        # 행
    j = goal                                      # 열
    while i > 0:                                  # 맨 윗줄에 도착하기 전까지 위로 올라가자
        i -= 1                                    # 위로 이동
        if j > 0 and ladder[i][j-1] == 1:         # 왼쪽칸이 있고 1이면
            while j > 0 and ladder[i][j-1] == 1:  # 사다리를 벗어나거나 0일 때까지
                j -= 1                            # 왼쪽 이동
        elif j < 99 and ladder[i][j+1] == 1:      # 오른쪽 칸이 1이면
            while j < 99 and ladder[i][j+1] == 1: # 사다리를 벗어나거나 0일 때까지
                j += 1                            # 오른쪽 이동
                                                  # 좌우가 0이면 위로
    return j                                      # 0번 행에 도착했을 때의 열(출발지점) 반환

# 라이브에서 작성한 코드
import sys
sys.stdin = open('input.txt')
T = 10
for tc in range(1, T+1):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    goal = 0                                                        # 도착지
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = solve(goal)
    print('#{} {}'.format(tc, ans))