import sys
sys.stdin = open('input.txt')

for T in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

# 거꾸로 올라가는 게 나을 수도?!
# 마지막 행에서 2를 찾고 위로 올라가면서 진행
# 1 따라 올라가면서 좌우 확인
# 옆에도 1이 있으면 1 있는 방향으로 행 꺾음

    # 시작점 초기화
    i = 99
    j = arr[99].index(2)
    k = 0

    # 위, 왼, 오 방향 설정
    di = [-1, 0, 0]
    dj = [0, -1, 1]

    while i > 0:
        if k == 0:
            if 1 < j <= 99 and arr[i][j-1] == 1: # 왼쪽에 길 있으면 방향 전환
                k = 1
                nj = j + dj[k]
                j = nj
            elif 0 <= j < 99 and arr[i][j+1] == 1: # 오른쪽에 길 있으면 방향 전환
                k = 2
                nj = j + dj[k]
                j = nj
            else: # 길 없으면 직진
                ni = i + di[k]
                nj = j + dj[k]
                i, j = ni, nj
        else: # 방향이 좌 또는 우인 상태
            if arr[i-1][j] == 1: # 위에 길 있으면 방향 전환하고 1칸 이동
                k = 0
                ni = i + di[k]
                i = ni
            else: # 위에 길 없으면 방향 유지한 채 이동
                nj = j + dj[k]
                j = nj

    print('#{} {}'.format(t, j))