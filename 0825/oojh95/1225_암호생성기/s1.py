import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    len_arr = len(arr)
    T = 1
    tmp = 1
    while tmp != 0:
        tmp = arr[0] - T
        T += 1
        if T == 6:
            T = 1
        if tmp <= 0:
            tmp = 0
        result = []
        for i in range(1, len_arr):
            result.append(arr[i])
        result.append(tmp)
        arr = result

    print('#{}'.format(tc), *arr)

