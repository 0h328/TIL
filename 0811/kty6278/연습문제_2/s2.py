# input 데이터를 불러온다.
import sys
sys.stdin = open('input2.txt')

testcase = int(input())
for _ in range(testcase):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]
    dr = [1, 0, -1, 0]
    dc = [0, -1, 0, 1]
    result = 0
    for i in range(n):
        for j in range(n):
            for k in range(4):
                if -1 < i + dc[k] < n and -1 < j + dr[k] < n:
                    result += abs(data[i + dc[k][j] + dr[k][j]] - data[i][j])
                else:
                    continue
    print('#{} {}'.format(testcase, result))
