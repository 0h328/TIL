import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [[0] * i for i in range(1, N+1)]   # [[0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]
    for i in range(N):
        pascal[i][0], pascal[i][-1] = 1, 1
    for j in range(2, N):
        for k in range(1, len(pascal[j]) - 1):
            pascal[j][k] = pascal[j-1][k-1] + pascal[j-1][k]
    print('#{}'.format(tc))
    for m in range(N):
        print(' '.join(map(str, pascal[m][:])))
