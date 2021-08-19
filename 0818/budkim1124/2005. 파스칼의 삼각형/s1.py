import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N = int(input())
    arr = []

    for x in range(1, N+1):
        line = []
        for y in range(x):
            line.append(0)
        arr.append(line)
    # print(arr)

    for n in range(0, N):
        for i in range(0, n+1):
            if n == 0:
                arr[n][0] = 1
            elif n != 0:
                arr[n][0] = 1
                arr[n][-1] = 1

    for n in range(2, N):
        for i in range(1, n):
            arr[n][i] += (arr[n-1][i-1] + arr[n-1][i])

    print("#{}".format(num+1), end="")
    for n in range(N):
        print("")
        for i in range(n+1):
            print(arr[n][i], end=" ")
    print("")