import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def Ladder(ladder):
    #좌우하
    dr = [0, 0, 1]
    dc = [-1, 1, 0]
    d_idx = [[2, 0], [2, 1], [0, 1, 2]] #왼쪽, 오른쪽, 아래쪽 방향
    d_now = 2 #처음 방향 = 아래쪽
    for X in range(1, 101):
        #출발지점인 경우
        if ladder[0][X] == 1:
            row, col = 1, X
            while row < 99:
                #direction 방향에 맞춰 탐색후 1이 보이면 이동
                for d in d_idx[d_now]:
                    if ladder[row + dr[d]][col + dc[d]] == 1 or ladder[row + dr[d]][col + dc[d]] == 2:
                        row += dr[d]
                        col += dc[d]
                        d_now = d
                        break
        #도착지가 2이면 idx - 1 return
        if ladder[row][col] == 2:
            return X - 1 #테두리 설정해줬기 때문에 1 빼줌
    return False

for t in range(1, 11):
    input()
    #idx 에러 안 나도록 테두리 설정
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    print('#{} {}'.format(t, Ladder(ladder)))