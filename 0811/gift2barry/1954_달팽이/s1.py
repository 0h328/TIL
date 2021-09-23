import sys
sys.stdin = open('input.txt')

T = int(input())

for testCase in range(1, T+1):
    # 테스트 케이스를 위한 배열 생성 및 초기화
    arr = [[0] * testCase] * testCase       # or arr = [[0]*testCase for _ in range(testCase)]

    #좌표:우,하, 좌,상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction = 0

    #초기 좌표
    x = y = 0
    arr[x][y] = 1

    #달팽이 시작
    #초기좌표가 있으니 range는 1 부터 시작, 2차원배열의 총 크기는 입력값의 제곱, 그리고 인덱스가 아님으로 1 추가
    for num in range(1, testCase**2 + 1):
        x += direction
        y += direction

        arr[x][y] = num     #숫자 채워넣기

        # 방향전환 타이밍:
        #

# n 을 만들고
# 2차원 배열 만들어준다
# 우 하 좌 상 순서로 방향 델타값 생성: [[1,0], [0,1], ..]
# cnt 는 4개 채우고 3개 채우고 2개 채우고 하는걸 카운트  cnt = n
# 방향전환을 하기 위한 포인트 가 check 변수
