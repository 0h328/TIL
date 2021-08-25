def versus(i, j):

    if i == j:
        return i

    a = versus(i, (i+j)//2)
    b = versus((i+j)//2+1, j)

    if card[a] == 1 and card[b] == 3: return a
    elif card[a] == 3 and card[b] == 1: return b
    elif card[a] < card[b]: return b
    else: return a


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = [0] + list(map(int, input().split()))

    print('#{} {}'.format(tc, versus(1, N)))
