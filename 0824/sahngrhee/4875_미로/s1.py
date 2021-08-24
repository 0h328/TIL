import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    mazeArray = [list(map(int, input())) for _ in range(N)]
    print(DataFrame(mazeArray))
    stack = []
    drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for i in range(N):
        for j in range(N):
            if mazeArray[i][j] == 2:
                start = [i, j]
    print(start)
    stack.append([start, drc[3]])
    print(stack)

    visit = []
    for i in range(2):
        visit.append(start[i] + drc[3][i])
    print(visit)
