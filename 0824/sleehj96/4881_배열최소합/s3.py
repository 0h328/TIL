import sys
sys.stdin = open('input.txt')


def down_min_num(idx):
    global min_val

    if idx == N:
        # print(sel)
        my_sum = 0
        for k in range(N):
            my_sum += grid[k][sel[k]]
            if my_sum >= min_val:
                return

        if min_val > my_sum:
            min_val = my_sum

    else:
        for i in range(N):
            if check[i] == 0:
                check[i] = 1
                sel[idx] = arr[i]
                down_min_num(idx+1)
                check[i] = 0


        # for i in range(idx, N):
        #     # print(idx, i)
        #     arr[idx], arr[i] = arr[i], arr[idx]
        #     down_min_num(idx + 1)
        #     arr[idx], arr[i] = arr[i], arr[idx]


T = int(input())
tc = 1
while tc <= T:
    N = int(input())
    grid = []

    for _ in range(N):
        grid.append(list(map(int, input().split())))
    # print(grid)

    arr = []
    for n in range(N):
        arr.append(n)

    sel = [0 for _ in range(N)]
    check = [0 for _ in range(N)]

    min_val = 9 * N

    down_min_num(0)

    print('#{0} {1}'.format(tc, min_val))
    # break
    tc += 1
