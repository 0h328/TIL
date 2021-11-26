import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    N = int(input())
    lst = [list([0]*10) for _ in range(10)]
    result = 0

    for n in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                lst[x][y] += 1

    for i in range(10):
        result += lst[i].count(2)

    print(result)
