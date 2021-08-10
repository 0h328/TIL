import sys
sys.stdin = open('input.txt')

def card(arr):
    counting = [0] * 10

    for i in arr:
        counting[i] += 1

    return 9 - counting[::-1].index(max(counting)), max(counting)

T = int(input())

for i in range(T):
    N = int(input())
    arr = list(map(int, list(input())))
    result = card(arr)
    print('#{} {} {}'.format(i + 1, result[0], result[1]))