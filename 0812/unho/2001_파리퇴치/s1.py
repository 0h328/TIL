import sys
sys.stdin = open('input.txt')


test_case = int(input())


for tc in range(1, test_case+1):
    n, m = map(int, input().split())
    answer = 0

    board = [list(map(int, input().split())) for _ in range(n)]     # 파리의 수 2차원 배열

    max_die = 0                                                     # 최대한 많이 죽은 파리

    for y in range(n-m+1):                                          # 보드판 행열 반복, 파리채의 시작점 인덱스
        for x in range(n-m+1):
            die = 0                                                 # 해당 영역의 파리채로 죽인 파리 수
            for r in range(y, y+m):
                for c in range(x, x+m):
                    die += board[r][c]
            if max_die < die:
                max_die = die

    print('#{} {}'.format(tc, max_die))