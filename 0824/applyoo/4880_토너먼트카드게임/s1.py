import sys
sys.stdin = open('input.txt')


def rcp(a, b):
    if a[0] == 1 and b[0] == 3: return a
    elif a[0] == 3 and b[0] == 1: return b
    elif a[0] < b[0]: return b
    else: return a


def tournament(arr):
    if len(arr) == 1:
        return arr[0]

    mid = (len(arr)//2) if len(arr) % 2 == 0 else (len(arr)//2) + 1
    left = tournament(arr[:mid])
    right = tournament(arr[mid:])

    return rcp(left, right)


T = int(input())
for test in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    cards = [[temp[i], i+1] for i in range(N)]

    print('#{} {}'.format(test+1, tournament(cards)[1]))
