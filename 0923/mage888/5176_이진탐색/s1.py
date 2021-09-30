import sys
sys.stdin = open('input.txt')

def in_order(n):
    global num

    if n <= N:
        if tree[n] == 0:
            in_order(n*2)
            num += 1
            tree[n] = num
            in_order(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    num = 0

    in_order(1)
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))
