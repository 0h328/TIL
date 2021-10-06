import sys
sys.stdin = open('input.txt')

dr = [0, 1]
dc = [1, 0]

def find_sol(r, c, t):
    global result
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < N and nc < N:
            if nr == N-1 and nc == N-1 and result > t+data[nr][nc]:
                result = t+data[nr][nc]
            else:
                if result < t+data[nr][nc]:
                    continue
                find_sol(nr, nc, t+data[nr][nc])

for T in range(int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 1e9
    find_sol(0,0, data[0][0])

    print('#{} {}'.format((T+1), result))

#1 15
#2 18
#3 33
