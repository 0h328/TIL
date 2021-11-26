import sys
sys.stdin = open('input.txt')


def binarysearch(arr, target, start, end):
    global cnt, switch
    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            cnt += 1
            break
        elif arr[mid] < target:
            start = mid + 1
            if switch == 1:
                break
            switch = 1
        else:
            end = mid - 1
            if switch == -1:
                break
            switch = -1
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    N_list.sort()
    M_list = list(map(int, input().split()))

    cnt = 0

    for i in range(M):
        switch = 0
        binarysearch(N_list, M_list[i], 0, N-1)
    print('#{} {}'.format(tc, cnt))
