import sys
import copy

sys.stdin = open('input.txt')

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]



def dfs(cnt, buck):
    global ans
    if cnt == N:
        temp_ans = 0
        for z in range(W):
            for q in range(H):
                if buck[q][z] != 0:
                    temp_ans += 1
        if temp_ans < ans:
            ans = temp_ans
        return

    for a in range(W):
        check = 0
        for b in range(H):
            if buck[b][a] == 0:
                continue
            else:
                first = copy.deepcopy(buck)
                que = [(b, a, buck[b][a])]

                while que:
                    temp = que.pop()
                    if temp[2] == 1:
                        buck[temp[0]][temp[1]] = 0
                    else:
                        buck[temp[0]][temp[1]] = 0
                        for c in range(1, temp[2]):
                            for i in range(4):
                                if 0 <= temp[0] + dx[i] * c < H and 0 <= temp[1] + dy[i] * c < W and buck[temp[0] + dx[i] * c][temp[1] + dy[i] * c] != 0:
                                    if (temp[0] + dx[i] * c, temp[1] + dy[i] * c, buck[temp[0] + dx[i] * c][temp[1] + dy[i] * c]) not in que:
                                        que.append((temp[0] + dx[i] * c, temp[1] + dy[i] * c, buck[temp[0] + dx[i] * c][temp[1] + dy[i] * c]))

                buck_down = [[0 for _ in range(W)] for _ in range(H)]
                for d in range(W):
                    temp = []
                    for e in range(H):
                        if buck[e][d]:
                            temp.append(buck[e][d])
                    for j in range(len(temp)):
                        buck_down[H-len(temp)+j][d] = temp[j]
                check = 1
            if check == 1:
                dfs(cnt+1,buck_down)
                buck = first
                break
    dfs(N,buck)



for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    buck_list = [list(map(int, input().split())) for _ in range(H)]
    ans = 987654321
    dfs(0, buck_list)
    print('#{} {}'.format(tc,ans))