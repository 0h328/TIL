import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    pascal = [[1] * i for i in range(1, N+1)]

    if N > 2:
        for n in range(2, N):           # 행의 범위
            for k in range(1, N-1):     # 열의 범위
                if n == k:              # n == k는 마지막 인덱스에 해당하므로 값이 변화되면 안됨.
                    break
                pascal[n][k] = pascal[n-1][k-1] + pascal[n-1][k]

    print('#{}'.format(tc))
    for i in range(N):
        print(*pascal[i])
