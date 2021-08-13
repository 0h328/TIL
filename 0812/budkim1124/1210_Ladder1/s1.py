import sys
sys.stdin = open('input.txt')

# 우선 숫자 1을 보고 따라가야한다.
# 기본적으로 아래로 내려간다.
# 오른쪽 또는 왼쪽에도 1이 나온다면 아래로 가는 것이 아닌
# 오른쪽 혹은 왼쪽으로 가는 선택을 해야한다.
# 배열의 array[i][0]에 해당하는 리스트 중 1인 곳을
# 모두 시작점으로 만든다.

def search(start): # 도착지에서 위로 올라가는 함수
    i = 99  # 행
    j = start   # 열
    while i > 0:    # 맨 윗줄에 도착하기 전까지 위로 올라감
        i -= 1  # 위로 한 칸 이동 (첫 번째 출발이다.)

        # 왼쪽 칸이 1이면
        if j > 0 and ladder[i][j-1] == 1:     # 왼쪽 칸이 1이면
            while j > 0 and ladder[i][j-1] == 1:   # 사다리를 벗어나거나 0을 만날 때까지 왼쪽으로 이동
                j -= 1

        # 오른쪽 칸이 1이면
        elif j < 99 and ladder[i][j + 1] == 1:
            # ㄴ 왼쪽 칸이 있고 사다리가 있으면 # j<99는 오른쪽 칸이 존재하는지 아닌지 확인하기 위해
            while j<99 and ladder[i][j + 1] == 1:
                j += 1
ㅡㅎ        # 좌우가 0이면 위로(출발지) 리턴

    return j # 0번 행에 도착했을 때의 열(출발지) 리턴

T = 10

for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착지 검색
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)
    print("#{} {}".format(tc, ans))