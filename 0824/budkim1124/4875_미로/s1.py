import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 3:
                a, b = i, j

    while arr[a][b] != 2:
        if 0<= a+1 <= N and 0<= b <= N and arr[a+1][b] == 0:
            arr[a+1][b] = 1
            a, b = a+1, b
        elif 0 <= a <= N and 0 <= b+1 <= N and arr[a][b+1] == 0:
            arr[a][b+1] = 1
            a, b = a, b+1
        elif 0<= a <= N and 0<= b-1 <= N and arr[a][b-1] == 0:
            arr[a][b-1] = 1
            a, b = a, b-1
        elif 0<= a-1 <= N and 0<= b <= N and arr[a-1][b] == 0:
            arr[a-1][b] = 1
            a, b = a, b-1
        else:
            print("#{} {}".format(num+1, 0))
            break

    print("#{} {}".format(num+1, 1))


