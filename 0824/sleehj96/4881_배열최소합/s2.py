import sys
sys.stdin = open('input.txt')


def down_min_num(idx):
    global min_val

    if idx == N:
        my_sum = 0
        for k in range(N):
            my_sum += grid[k][sel[k]]
            if my_sum >= min_val:
                return

        if min_val > my_sum:
            min_val = my_sum

    else:
        for i in range(idx, N):
            # print(idx, i)
            sel[idx], sel[i] = sel[i], sel[idx]
            down_min_num(idx + 1)
            sel[idx], sel[i] = sel[i], sel[idx]


T = int(input())
tc = 1
while tc <= T:
    N = int(input())
    grid = []

    for _ in range(N):
        grid.append(list(map(int, input().split())))
    # print(grid)

    sel = []
    for n in range(N):
        sel.append(n)
    min_val = 9*N
    down_min_num(0)

    print('#{0} {1}'.format(tc, min_val))
    # break
    tc += 1
