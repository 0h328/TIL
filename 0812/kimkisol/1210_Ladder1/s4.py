import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#라이브 강의 답
def Ladder(ladder):
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
            break
    i = 99
    j = goal
    while i > 0:
        i -= 1
        if j > 0 and ladder[i][j - 1] == 1:
            while j > 0 and ladder[i][j - 1] == 1:
                j -= 1
        elif j < 99 and ladder[i][j + 1] == 1:
            while j < 99 and ladder[i][j + 1] == 1:
                j += 1
    return j

for t in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    print('#{} {}'.format(t, Ladder(ladder)))