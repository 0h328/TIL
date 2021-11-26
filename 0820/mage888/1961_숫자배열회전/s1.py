import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]

    arr2 = [['' for _ in range(N)] for _ in range(N)]

    arr90 = ['' for _ in range(N)]
    arr180 = ['' for _ in range(N)]
    arr270 = ['' for _ in range(N)]

    for i in range(N):
        for j in range(N):
            arr90[i] += (arr[N-1-j][i])
            arr180[i] += (arr[N-1-i][N-1-j])
            arr270[i] += (arr[j][N-1-i])

    print(arr90)
    print(arr180)
    print(arr270)

    print('#{}'.format(tc))
    for i in range(len(arr)):
        print(''.join(arr90[i]), ''.join(arr180[i]), ''.join(arr270[i]))