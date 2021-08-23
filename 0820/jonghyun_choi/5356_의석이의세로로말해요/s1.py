import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    grid = [[0]*15 for _ in range(5)]
    word = [list(map(str,input())) for _ in range(5)]
    for i in range(len(word)):
        for j in range(len(word[i])):
            grid[i][j] = word[i][j]
    print('#{}'.format(case + 1), end=' ')
    for i in range(15):
        for j in range(len(grid)):
            if grid[j][i] != 0:
                print(grid[j][i], end='')
    print()
