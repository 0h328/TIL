import sys
sys.stdin = open('input.txt')

def cafe(x,y,cnt):
    global ans, flag
    check = 0
    if cafe_list[y][x] not in que:
        que.append(cafe_list[y][x])
        if cnt == 0:
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                flag = i
                if 0 <= new_x < N and 0 <= new_y < N:
                        cafe(new_x, new_y, cnt + 1)
        elif cnt != 0:
            new_x = x + dx[flag%4]
            new_y = y + dy[flag%4]
            if 0 <= new_x < N and 0 <= new_y < N:
                cafe(new_x, new_y, cnt + 1)
            else:
                while True:
                    flag += 1
                    new_x = x + dx[flag % 4]
                    new_y = y + dy[flag % 4]
                    if 0 <= new_x < N and 0 <= new_y < N:
                        cafe(new_x, new_y, cnt + 1)
                    break

    else:
        if start_x == x and start_y == y:
            temp_ans = len(que)
            if ans < temp_ans:
                ans = temp_ans


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cafe_list = [list(map(int,input().split())) for _ in range(N)]
    dy = [1,1,-1,-1]
    dx = [-1,1,1,-1]
    ans = -1
    flag = 0
    for a in range(N):
        for b in range(N):
            que = []
            start_x, start_y = a,b
            cafe(a,b,0)
    print(ans)