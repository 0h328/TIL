def versus(i, j):

    a = versus(i, (i+j)//2)
    b = versus((i+j)//2+1, j)

    if card[a] == 1:
        if card[b] == 1:
            return a
        elif card[b] == 2:
            return b
        elif card[b] == 3:
            return a

    if card[a] == 2:
        if card[b] == 1:
            return a
        elif card[b] == 2:
            return a
        elif card[b] == 3:
            return b

    if card[a] == 3:
        if card[b] == 1:
            return b
        elif card[b] == 2:
            return a
        elif card[b] == 3:
            return a

    # 뎁스에러 뜨는이유가 뭘까?

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))

    print('#{} {}'.format(tc, versus(1, N)))
