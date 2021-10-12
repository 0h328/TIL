def solve(room_num):
    if room_num == 1:                                   # 1번 방이면 바로 1 반환 (시작 지점)
        return 1
    else:
        for i in range(4):                              # 4방 탐색
            nr = starting[room_num][0] + dr[i]          # room_num으로부터 4방 이동
            nc = starting[room_num][1] + dc[i]

            if (0 <= nr < N) and (0 <= nc < N):         # 이동 하려는 곳의 범위 체크하고
                if arr[nr][nc] == room_num-1:           # 만약 이동하려고 하는 곳이 1 작고 (더 작은 숫자 순서로 찾아가기)
                    if visited[room_num-1]:             # 방문을 한 곳이라면
                        return visited[room_num-1] + 1  # 갈 수 있는 루트 추가
                    # return solve(room_num-1) + 1
        return 1

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]       # N개의 줄에 주어지는 수 -> arr[r][c]는 모두 다른 수
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    visited = [0] * (N*N+1)                                         # 방문 여부 체크 (인덱스 고려)
    starting = [0] * (N*N+1)                                        # 시작 지점을 잠는 배열 (인덱스 고려)

    for r in range(N):                                              # 시작 지점 초기화
        for c in range(N):  
            starting[arr[r][c]] = (r, c)                            # ex. 1번방: (1, 1) / 2번방: (2, 2)

    for room_num in range(1, N*N+1):                                # 1 ~ N*N까지 방문
        visited[room_num] = solve(room_num)

    max_num = max_val = 0
    for idx, num in enumerate(visited, start=1):                    # 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력
        if num > max_num:                                           # 이동하려는 방이 크면
            max_num = num                                           # 값 갱신하고
            max_val = idx - num                                     # 연속한 1의 개수 -> 연속으로 1이 커지는 구간의 길이
    print('#{} {} {}'.format(tc, max_val, max_num))