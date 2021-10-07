import sys
sys.stdin = open('input.txt')


def split(arr):
    if len(arr) < 2: return arr
    l = split(arr[:len(arr) // 2])
    r = split(arr[len(arr) // 2:])
    return merge(l, r)


def merge(le, ri):
    global cnt
    res = []
    x1 = x2 = 0

    while len(le) != x1 and len(ri) != x2:
        if le[x1] <= ri[x2]:
            res.append(le[x1])
            x1 += 1
        else:
            res.append(ri[x2])
            x2 += 1

    if len(le) > x1:
        cnt += 1
        res.extend(le[x1:])
    else:
        res.extend(ri[x2:])

    return res


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    arr = split(arr)

    ans.append('#{0} {1} {2}'.format(tc, arr[N//2], cnt))

print(*ans, sep='\n')
