import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    # print(arr)

    rotation90 = []
    for j in range(N):
        tmp = []
        for i in range(N-1, -1, -1):
            tmp.append(arr[i][j])
        rotation90.append(tmp)
    # print(rotation90)

    rotation180 = []
    for i in range(N-1, -1, -1):
        tmp = []
        for j in range(N-1, -1, -1):
            tmp.append(arr[i][j])
        rotation180.append(tmp)
    # print(rotation180)

    rotation270 = []
    for j in range(N-1, -1, -1):
        tmp = []
        for i in range(N):
            tmp.append(arr[i][j])
        rotation270.append(tmp)
    # print(rotation270)

    print('#{}'.format(tc))
    for k in range(N):
        print(''.join(rotation90[k]), ''.join(rotation180[k]), ''.join(rotation270[k]))
