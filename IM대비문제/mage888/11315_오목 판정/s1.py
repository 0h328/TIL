import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(input()) for _ in range(N)]

    dr = [0, 1, 1, 1]
    dc = [1, 1, 0, -1]

    result = 'NO'
    for r in range(N):
        for c in range(N):
            if data[r][c] == 'o':
                for k in range(4):
                    nr = r + dr[k]
                    nc = c + dc[k]
                    cnt = 1
                    while True:
                        if nr in range(N) and nc in range(N) and data[nr][nc] == 'o':
                            nr = nr + dr[k]
                            nc = nc + dc[k]
                            cnt += 1
                        else:
                            break
                    if cnt >= 5:
                        result = 'YES'
                        break

    print('#{} {}'.format(tc, result))




# tc때문에 전수 조사한다. 'o'를 만나면 조사를 시작
# 기준점은 'o'
# 'o'를 기준으로 상하좌우 모두 조사.
# DFS방식으로 조사를 한다.
# 내가 현재 조사하고 있는 '방향'을 기준으로 조사한다.
# (상 하) (좌 우) (좌상 우하) (우상 좌하)를 모두 조사한다.
# 좌표, 조사할 방향, 이어진 돌의 개수
# def DFS(x, y, idx, cnt)
    # 조사할 대상
    # 해당 방향으로 끝까지 조사
    # 범위를 벗어나기전, 해당 위치에 돌이 있을때 동안 # nx = x + dx[i]
        # 범위를 벗어나지도 않고, 돌도 있다면
        # 이어진 돌의 개수 + 1
        # 다음 위치 조사 # nx = nx + dx[i]

    # 나와 세트인 반대 방향도 똑같은 조건으로 조사

    # 모든 방향에 대한 조사 후에, 이어진 돌의 개수 반환

# 모든 위치에 대한 조사
# 단, 해당 좌표의 값이 'o'라면.
# 처음 조사를 할때, 내 위치도 돌이기 때문에 1
# cnt = DFS(x, y, k, 1)
# 만약 반환 받은 값이 5 이상이 된다면 -> 한줄이라도 5 이상이 됐다면
    # YES
    # 조사 종료