import sys
sys.stdin = open('input.txt')


def down_min_num(idx):
    if idx == N:
        ans = 0
        for k in range(N):
            ans += grid[k][sel[k]]
        print(sel, ans)
        ans_list.append(ans)

    else:
        for i in range(idx, N):
            # print(idx, i)
            sel[idx], sel[i] = sel[i], sel[idx]
            down_min_num(idx+1)
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
    ans_list = []
    # my_sum = 0      # 누적시킬 공간
    down_min_num(0)
    # print(ans_list)
    # print(min(ans_list))

    print('#{0} {1}'.format(tc, min(ans_list)))
    # break
    tc += 1

