import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    x_direction = [1, 0, -1, 0]    # 우하좌상
    y_direction = [0, 1, 0, -1]    # 우하좌상
    action = 0  # 방향
    x_idx, y_idx = 0, 0  # 시작 위치
    arr[y_idx][x_idx] = 1  # 1행 1열을 1로 고정하고 시작
    idx = 2  # 위에 1이 있으니 2부터 시작

    while idx <= N * N:
        next_x = x_idx + x_direction[action]
        next_y = y_idx + y_direction[action]
        # 범위를 벗어났거나 이미 값이 있을 때 방향 전환
        if (next_x < 0 or next_x > N - 1) or (next_y < 0 or next_y > N - 1) or arr[next_y][next_x] != 0:
            action = (action + 1) % 4
            continue
        x_idx = next_x
        y_idx = next_y
        arr[y_idx][x_idx] = idx
        idx += 1

    print('#{}'.format(tc))
    for x in range(N):
        for y in range(N):
            print(arr[x][y], end=' ')
        print()









