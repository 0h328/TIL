def direc(r, c, move, l):
    global flag
    if n_list[r][c] != 0:
        flag = 1
    if flag == 1:
        return

    if n_list[r][c] == 0:
        if r == 0:          # 상
            direc_list[r + move][c].append(1)
            direc_list[r + move][c].append(move)
        elif r == N - 1:    # 하
            direc_list[r - move][c].append(2)
            direc_list[r - move][c].append(move)
        elif c == 0:        # 좌
            direc_list[r][c + move].append(3)
            direc_list[r][c + move].append(move)
        elif c == N - 1:    # 우
            direc_list[r][c - move].append(4)
            direc_list[r][c - move].append(move)

    if 0 < r < N - 1 and 0 < c < N - 1:
        if l == 0:
            direc(r - 1, c, move + 1, l)
        elif l == 1:
            direc(r + 1, c, move + 1, l)
        elif l == 2:
            direc(r, c - 1, move + 1, l)
        elif l == 3:
            direc(r, c + 1, move + 1, l)


def core():
    for new in new_list:
        i = new[0]
        j = new[1]
        c = new[2]

        temp_dict = {}
        for x in range(1, c, 2):
            direction = direc_list[i][j][x]
            move = direc_list[i][j][x + 1]
            temp_dict[direction] = move
        temp_dict = sorted(temp_dict.items(), key = lambda x:x[1])

        for ct in range((c - 1)//2):
            flag = 0
            current = temp_dict[ct][0]
            zero_cnt = temp_dict[ct][1]

            if current == 1:
                for n in range(0, i):
                    if n_list[n][j] != 0:
                        flag = 1
                        break
                if flag == 0:
                    for n in range(0, i):
                        n_list[n][j] = 2
                    break
            elif current == 2:
                for n in range(i + 1, N):
                    if n_list[n][j] != 0:
                        flag = 1
                        break
                if flag == 0:
                    for n in range(i + 1, N):
                        n_list[n][j] = 2
                    break
            elif current == 3:
                if n_list[i][0:j] == [0] * zero_cnt:
                    n_list[i][0:j] = [2] * zero_cnt
                    break
            elif current == 4:
                if n_list[i][j + 1:N] == [0] * zero_cnt:
                    n_list[i][j + 1:N] = [2] * zero_cnt
                    break

tc = int(input())

for t in range(1, tc + 1):
    result = 0
    cnt = 0
    N = int(input())
    n_list = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    direc_list = [0] * N
    for m in range(N):
        direc_list[m] = []
        for n in range(N):
            direc_list[m].append([0])

    new_list = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if n_list[i][j] == 1:
                for l in range(4):
                    nr = i + dr[l]
                    nc = j + dc[l]
                    flag = 0

                    direc(nr, nc, 1, l)

                if len(direc_list[i][j]) > 1:
                    new_list.append([i, j, len(direc_list[i][j])])
                    new_list = sorted(new_list, key = lambda x : x[2])
    core()

    for i in range(N):
        for j in range(N):
            if n_list[i][j] == 2:
                result += 1

    print("#{} {}".format(t, result))