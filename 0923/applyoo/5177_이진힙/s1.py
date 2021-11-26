import sys
sys.stdin = open('input.txt')


def heap_push(n):
    global idx
    idx += 1
    q[idx] = n
    p, c = idx // 2, idx

    while p and q[p] > q[c]:
        q[p], q[c] = q[c], q[p]
        p, c = p // 2, p


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    q = [0] * (N+1)
    idx = 0
    for v in arr:
        heap_push(v)

    ans = 0
    while idx:
        idx //= 2
        ans += q[idx]

    print('#{0} {1}'.format(tc, ans))
