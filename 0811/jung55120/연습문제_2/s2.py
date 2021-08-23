import sys
sys.stdin = open('input2.txt')

T = int(input())                    # testcase 값을 먼저 받아 옴
for n in range(1,T+1) :             # testcase 횟수만큼 반복
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]              # 상하좌우 구하기 위해서 만들어준 임의의 좌표
    dc = [0, 0, -1, 1]

    result = []                     # 빈 result 만들기
    for i in range(N):              # n * n 배열 만큼 반복
        for j in range(N):
            r = i
            c = j
            check_list = []
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if (0 <= nr < N) and (0 <= nc < N):
                    check_list.append(abs(data[nr][nc]-data[i][j]))

                if nr < 0 or nr >= N or nc < 0 or nc >= N:
                    continue
            result.append(sum(check_list))
    print('#{0} {1}'.format(n,sum(result)))
