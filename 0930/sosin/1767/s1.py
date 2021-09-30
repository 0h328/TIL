import sys
sys.stdin = open('input.txt')

dr = [-1,1,0,0]
dc = [0,0,-1,1]

# 위일 때, 0
# 아래일 때, N-1
# 왼쪽일 떄, 0
# 오른쪽일 때, N-1
def dfs(core_idx, cnt):
    global result
    if core_idx >= len(cores):
        if result > cnt:
            [print(p) for p in processor]
            print(cnt)
            result = cnt
        return
    # 코어에 연결이 가능한 경우
    # 코어에 연결이 불가능한 경우
    
    r, c = cores[core_idx]
    for k in range(4):
        i = 1
        while True:
            nr = r + dr[k] * i
            nc = c + dc[k] * i

            if 0<=nr<N and 0<=nc<N and not processor[nr][nc]:
                # 가로 세로 방향 체크
                if k in [0,1]:
                    processor[nr][nc] = 2
                    if nr in [0, N-1]:
                        dfs(core_idx+1, cnt+i)
                        break
                else:
                    processor[nr][nc] = 3
                    if nc in [0, N-1]:
                        dfs(core_idx+1, cnt+i)
                        break
            else:
                break

            i+=1
        
        # 다시 원복
        while True:
            nr = r - dr[k] * i
            nc = c - dc[k] * i
            processor[nr][nc] = 0
            i-=1


for T in range(int(input())):
    N = int(input())
    result = 1e9

    processor = [list(map(int, input().split())) for _ in range(N)]
    cores = []
    for i in range(N):
        for j in range(N):
            if processor[i][j] == 1:
                if i not in [0, N-1] and j not in [0, N-1]:
                    cores.append((i,j))
    print(cores)
    dfs(0, 0)

    print('#{} {}'.format((T+1), result))


#1 12
#2 10
#3 24
