import sys

sys.stdin = open('input.txt')

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def break_buck(a):
    global check
    while a:
        b = a.pop()
        if 0 <= b[0] < N and 0 <= b[1] < N:
            if new_buck_list[b[0]][b[1]] != 1:
                new_buck_list[b[0]][b[1]] = 0
                if new_buck_list[b[0]][b[1]] != 0:
                    for i in range(1,new_buck_list[b[0]][b[1]]):
                        for c in range(4):
                            a.append([b[0]+dx[c]*e],[b[0]+dy[c]*e])
    else:
        return


def dfs(a, cnt):
    global ans, check
    if cnt == N:
        temp_ans = 0
        for a in range(W):
            for b in range(H):
                if new_buck_list[a][b] != 0:
                    temp_ans += 1
        if temp_ans < ans:
            ans = temp_ans
        return

    for c in range(H):
        if check == 1:
            break
        que.append([a,c])
        break_buck(que)
    check = 0
    for a in range(W):
        for b in range(H):
            if new_buck_list[a][b] == 1:
                for c in range(H-1,0,-1):
                    if new_buck_list[a][c] == 0:
                        if b < c:
                            new_buck_list[a][b], new_buck_list[a][c] = 0,1


    for d in range(W):
        dfs(d, cnt+1)




for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    buck_list = [list(map(int, input().split())) for _ in range(H)]
    new_buck_list = list(map(list, zip(*buck_list)))
    ans = 987654321
    check = 0
    que = []
    for c in range(W):
        dfs(c,1)
    print(ans)