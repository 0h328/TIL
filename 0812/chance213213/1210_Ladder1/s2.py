import sys
sys.stdin = open('input.txt')

def search(start):
    i = 99
    j = start
    while i > 0:
        i -= 1
        if j > 0 and ladder[i][j-1] == 1: # 왼쪽 칸이 1이면
            while j > 0 and ladder[i][j-1] == 1:
                j -= 1
        elif j < 99 and ladder[i][j+1] == 1:
            while j < 99 and ladder[i][j+1] == 1:
                j += 1
    return j



T = 10
for tc in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)
    print('#{} {}'.format(tc, ans))