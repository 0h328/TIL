import sys
# from pandas import DataFrame

sys.stdin = open('input.txt')


T = int(input())
idx = 1

while idx <= T:
    N = int(input())
    paper_list = []
    ans = 0

    grid = [[[0 for _ in range(2)] for _ in range(10)] for _ in range(10)]
    # 처음에 grid = [[0, 0] * 10 for _ in range(10)] 으로 구현했다가
    # 얕은 복사가 일어나서 한참 헤멤
    # 위치도 while 바깥문에 썼다가 골치아팠음
    # print(grid)

    while N > 0:
        paper_list.append(list(map(int, input().split())))
        N -= 1

    # print(paper_list)
    for e in paper_list:
        if e[4] == 1:
            for r in range(e[0], e[2] + 1):
                for c in range(e[1], e[3] + 1):
                    grid[r][c][0] = 1

        elif e[4] == 2:
            for r in range(e[0], e[2] + 1):
                for c in range(e[1], e[3] + 1):
                    grid[r][c][1] = 1

    # print(DataFrame(grid))
    for r in range(10):
        for c in range(10):
            if grid[r][c][0] and grid[r][c][1]:
                ans += 1

    print('#{0} {1}'.format(idx, ans))
    # break
    idx += 1
