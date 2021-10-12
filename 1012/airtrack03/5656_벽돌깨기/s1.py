import sys

sys.stdin = open("input.txt")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bomb(data, n, k, cnt):
    global ans
    if k == n:  # 구슬 떨어뜨린 횟수가 n과 같아지면
        if cnt > ans:
            ans = cnt
        return

    start_cnt = cnt
    for col in range(W):  # 컬럼 순으로 탐색
        new_data = [data[r][:] for r in range(H)]  # 원본 데이터 수정하지 않기 위해 복사
        cnt = start_cnt
        for row in range(H):
            if data[row][col]:
                start = (row, col, data[row][col])  # 0이 아닌 지점에서 첫 벽돌 만남
                break
        else:  # 0이 아닌 블록 없다면
            continue  # 다음 컬럼으로 넘어감

        stack = [start]

        while stack:
            cur_row, cur_col, num = stack.pop()
            if new_data[cur_row][cur_col]:
                new_data[cur_row][cur_col] = 0
                cnt += 1

            for d in range(4):  # 4방향 탐색하며
                for i in range(1, num):
                    nxt_row = cur_row + dr[d] * i
                    nxt_col = cur_col + dc[d] * i
                    if 0 <= nxt_row < H and 0 <= nxt_col < W and new_data[nxt_row][nxt_col]:
                        if new_data[nxt_row][nxt_col] > 1:
                            stack.append((nxt_row, nxt_col, new_data[nxt_row][nxt_col]))
                            new_data[nxt_row][nxt_col] = 0
                        else:  # 1인 경우
                            new_data[nxt_row][nxt_col] = 0
                        cnt += 1

        if cnt == og_cnt:  # 중간에 모두 깨면 바로 함수 종료
            ans = cnt
            return
        clear_data(new_data)  # 중간에 0 값 없애줌
        bomb(new_data, n, k + 1, cnt)


def clear_data(data):
    for col in range(W):
        zero_idx = H - 1  # 제일 밑에서부터 0인 곳 탐색
        while zero_idx >= 0:
            while data[zero_idx][col] != 0:
                zero_idx -= 1
                if zero_idx < 0:  # 0인 곳 없으면 중단
                    break
            if zero_idx < 0:  # 0인 곳 없으면 중단
                break
            for i in range(zero_idx - 1, -1, -1):  # 0인 곳 다음 인덱스부터 0이 아닌 곳 탐색
                if data[i][col] != 0:  # i가 0이 아닌 곳 인덱스
                    break
            else:  # 0이 아닌 곳 못 찾으면 break
                break
            data[i][col], data[zero_idx][col] = (
                data[zero_idx][col],
                data[i][col],
            )  # 중간에 있는 0과 그 뒤 0이 아닌 곳 교환


T = int(input())

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    data = []
    og_cnt = 0  # 처음 0이 아닌 블록의 수
    for row in range(H):
        temp = list(map(int, input().split()))
        data.append(temp)
        for col in range(W):
            if temp[col] != 0:
                og_cnt += 1

    if og_cnt == 0:  # 블록 전부 0이면 바로 0 출력
        print("#{} {}".format(tc, 0))
    else:
        ans = 0  # 깨진 최대 블록의 수

        bomb(data, N, 0, 0)

        print("#{} {}".format(tc, og_cnt - ans))
