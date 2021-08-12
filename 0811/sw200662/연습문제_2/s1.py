import sys
sys.stdin = open('input.txt')

T = int(input())
for k in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    r = 0
    c = 0
    ans = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    cnt = 0
    while cnt < N*N:
        for i in range(4):
            nr = r + dr[i] # r로부터 dr만큼 이동한 새로운 nr
            nc = c + dc[i] # c로부터 dc만큼 이동한 새로운 nc

            #1. 벽 안으로 들어오는 경우만 수행
            if (0 <= nr < N) and (0 <= nc < N):
                ans += abs(data[r][c]-data[nr][nc])

        #2. 벽 밖으로 나가면 그냥 continue > 필요없는
        #    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        #        continue
        c += 1 # 오른쪽으로 한칸씩 이동
        cnt += 1 # cnt값을 하나씩 늘려서 while문의 cnt조건시 종료
        if c >= N: # C값이 N값에 도달하면, 나간것이므로
            c = 0 # C값을 0으로 초기화시켜주고
            r += 1 # 아래로 한칸 이동

    print(ans)