import sys
sys.stdin = open('input.txt')

def cnt_subtree(value):
    global cnt

    if value:
        cnt += 1
        cnt_subtree(left[value])
        cnt_subtree(right[value])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    edge = list(map(int, input().split()))
    # print(edge)
    left = [0] * (E+2)
    right = [0] * (E+2)
    cnt = 0

    for i in range(E):
        p, c = edge[i*2], edge[i*2+1]   # parent, child

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt_subtree(N)
    print('#{} {}'.format(tc, cnt))






