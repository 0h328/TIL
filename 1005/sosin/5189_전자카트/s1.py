import sys
sys.stdin = open('input.txt')

from itertools import permutations

for T in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 1e9
    for selects in permutations(range(1, N), N-1):
        first = 0
        temp = 0
        selects = list(selects) + [0]
        for s in selects:
            temp += data[first][s]
            if result < temp:
                break
            else:
                first = s
        else:
            result = temp

    print('#{} {}'.format((T+1), result))

#1 89
#2 96
#3 139