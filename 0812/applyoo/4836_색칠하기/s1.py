import sys
sys.stdin = open('input.txt')

def painting():
    paper = [[0]*10 for _ in range(10)]     # 맵 구현?

    for x1, y1, x2, y2, color  in arr:
        if color == 1:                      # 빨강인 경우(1: 빨강, 2: 파랑, 3: 보라)
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if paper[x][y]:         # 이미 칠해져 있는 경우
                        paper[x][y] = 3     # 보라색 칠하기
                    else:                   # 칠해져 있지 않은 경우
                        paper[x][y] = 1     # 빨간색 칠하기
        else:                               # 파랑인 경우(빨강의 경우와 동일하게 실행)
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    if paper[x][y]:
                        paper[x][y] = 3
                    else:
                        paper[x][y] = 1

    return sum(paper, []).count(3)

T = int(input())
for test in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(test+1, painting()))