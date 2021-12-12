'''
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

2 2 3 4 => (2,2)에서 (3,4)까지의 합을 구해라.

구간 합(누적 합) 구하는 법.

arr =
1 2 3 4
2 3 4 5
3 4 5 6

알아보기 쉽게 인덱스 시작을 (1,1)이라 치고, arr[3][4]는 arr[1][1]부터 arr[3][4]까지 모든 배열을 누적으로 합한 값이다.
즉, arr[3][4] = [1+2+3+4]+[2+3+4+5]+[3+4+5+6]이다.

(2,2)에서 (3,4)까지를 D,
(1,1)을 A,
(1,2)과 (1,4)의 범위를 B ,
(2,1)과 (3,1)의 범위를 C라하면,
arr[3][4]는 A+B+C+D를 모두 더한 값이다.

여기서 D는 arr[3][4] (42)에서 B를 빼주고 C를 빼주면 된다.
하지만, 행끼리 합과 열끼리 합을 다 누적해주기 때문에 결국 D = arr[3][4] - B - C + A 이다.
'''

import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().strip().split())
arr = [[0] * (N+1)] + [[0] + list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

for i in range(1, N+1):
    for j in range(1, N):
        arr[i][j+1] += arr[i][j]    # 행끼리 누적

for j in range(1, N+1):
    for i in range(1, N):
        arr[i+1][j] += arr[i][j]    # 열끼리 누적

for _ in range(M):                  # arr[x2][y2]는 arr[1][1]부터 누적으로 값이 합쳐진 상태
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])

