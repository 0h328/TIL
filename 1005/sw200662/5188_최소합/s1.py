import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(x,y):
    global ans, temp_ans
    if ans < temp_ans:
        return
    if x == N - 1 and y == N - 1:
        if ans > temp_ans:
            ans = temp_ans
    dx = [0,1]
    dy = [1,0]

    for i in range(2):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if new_x < N and new_y < N and visit_list[new_x][new_y] == 0:
            temp_ans += list_num[new_x][new_y]
            visit_list[new_x][new_y] = 1
            dfs(new_x,new_y)
            temp_ans -= list_num[new_x][new_y]
            visit_list[new_x][new_y] = 0




for tc in range(1,T+1):
    N = int(input())
    list_num = [list(map(int,input().split())) for _ in range(N)]
    visit_list = [[0] * N for _ in range(N)]
    x = y = 0
    ans = 5000
    temp_ans = list_num[0][0]
    dfs(0,0)
    print('#{} {}'.format(tc,ans))

