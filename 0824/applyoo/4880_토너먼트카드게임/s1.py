import sys
sys.stdin = open('input.txt')


def rcp(a, b):
    if a == 1 and b == 3: return 0
    elif a == 3 and b == 1: return 1
    elif a < b: return 1
    else: return 0


def tournament(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        win = rcp(arr[0][0], arr[1][0])
        return arr[win]

    mid = (len(arr)//2) if len(arr) % 2 == 0 else (len(arr)//2) + 1
    left = tournament(arr[:mid])
    right = tournament(arr[mid:])

    win = rcp(left[0], right[0])
    if win == 0:
        return left
    else:
        return right


T = int(input())
for test in range(T):
    N = int(input())
    temp = list(map(int, input().split()))
    cards = [[temp[i], i+1] for i in range(N)]

    print('#{} {}'.format(test+1, tournament(cards)[1]))
