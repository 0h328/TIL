import sys
sys.stdin = open('input.txt')

T = int(input())
tc = 1
while tc <= T:

    N, M = map(int, input().split())        # 화덕크기 N, 피자 개수 M
    Ci = list(map(int, input().split()))

    print(Ci)
    cnt_list = [0] * M
    for idx, cheese in enumerate(Ci):
        for expo in range(1, 6):
            if cheese < 2 ** expo:
                cnt_list[idx] = expo
                break

    print(cnt_list)

    pizza_idx = N
    oven_idx = 0
    oven = cnt_list[:N]
    min_data = min(oven)

    while True:
        oven[oven_idx] -= min_data

        if oven[oven_idx] == 0:
            oven[oven_idx] = cnt_list[pizza_idx]
            min_data = min(oven)
            pizza_idx += 1

        if pizza_idx == M:

            if not any(oven):
                ans = pizza_idx

        oven_idx = (oven_idx + 1) % 3

    # q = list(cnt_list[:N])
    # index_q = [i for i in range(N)]
    # pizza_idx = N
    # fire_pit_idx = 0
    # while True:
    #     print(q, fire_pit_idx, pizza_idx)
    #     print(index_q)
    #     q[fire_pit_idx] -= 1
    #
    #     if q[fire_pit_idx] == 0:
    #         if pizza_idx < M:
    #             q[fire_pit_idx] = cnt_list[pizza_idx]
    #             index_q[fire_pit_idx] = pizza_idx
    #             pizza_idx += 1
    #
    #     else:
    #         q[fire_pit_idx] -= 1
    #
    #     if not any(q):
    #         ans = index_q[fire_pit_idx] + 1
    #         break

        # fire_pit_idx = (fire_pit_idx + 1) % N
        # break

    # print('#{0} {1}'.format(tc, ans))
    break
    tc += 1
