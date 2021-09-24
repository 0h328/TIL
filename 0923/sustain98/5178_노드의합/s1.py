import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n, m, l = map(int, input().split())
    res = 0
    for _ in range(m):
        node, val = map(int, input().split())
        while node > 1:
            node //= 2
            if node == l:
                res += val
    print('#{} {}'.format(idx, res))