tc = int(input())

for t in range(1, tc + 1):
    result = 0

    N = int(input())
    n_list = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]

                if 0<= nr <=N:


    print("#{} {}".format(t, result))