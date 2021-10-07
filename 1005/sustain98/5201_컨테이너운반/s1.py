import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    w_list = list(map(int, input().split()))
    t_list = list(map(int, input().split()))
    w_list.sort(reverse=True)
    t_list.sort(reverse=True)

    w_idx, t_idx = 0, 0
    res = 0
    while t_idx < m and w_idx < n:
        if t_list[t_idx] >= w_list[w_idx]:
            res += w_list[w_idx]
            t_idx += 1
        w_idx += 1
    print('#{} {}'.format(idx, res))

