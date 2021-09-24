import sys
sys.stdin = open('input.txt')


# thought process:
# temp 로 리스트 하나 만들어서, 거기서 숫자별로 중위 순회
# 큰건 우측, 작은건 좌측으로 새 트리 리스트에 배정


def in_order(n):
    global cnt
    if n:
        cnt += 1
        in_order(l[n])
        # cnt += 1
        in_order(r[n])
        # cnt += 1
    return


for tc in range(1, int(input())+1):
    N = int(input())
    tree = [0] * (N+2)

    for i in range(1, N+1):
        p, c = tree[i*2], tree[i*2+1]
        if l[p] == 0:
            l[p] = c
        else:
            r[p] = c

    in_order(N)
    print('#{} {}'.format(tc, cnt))