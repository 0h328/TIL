import sys

sys.stdin = open('input.txt')
# 생각을 잘못했다

def cafe(x, y, flag, cnt):
    global ans
    if cnt == 0:
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < N:
                if cafe_list[new_y][new_x] not in que:
                    que.append(cafe_list[new_y][new_x])
                    cafe(new_x, new_y, i, cnt + 1)
                    que.pop(-1)
                else:
                    if start_x == new_x and start_y == new_y:
                        temp_ans = len(que)
                        if ans < temp_ans:
                            ans = temp_ans
    elif cnt != 0:
        new_x = x + dx[flag % 4]
        new_y = y + dy[flag % 4]
        if 0 <= new_x < N and 0 <= new_y < N:
            if cafe_list[new_y][new_x] not in que:
                que.append(cafe_list[new_y][new_x])
                cafe(new_x, new_y, flag, cnt + 1)
                que.pop(-1)
            else:
                if start_x == new_x and start_y == new_y:
                    temp_ans = len(que)
                    if ans < temp_ans:
                        ans = temp_ans
        else:
            check = 0
            while check < 1:
                flag += 1
                check += 1
                new_x = x + dx[flag % 4]
                new_y = y + dy[flag % 4]
                if 0 <= new_x < N and 0 <= new_y < N:
                    if cafe_list[new_y][new_x] not in que:
                        que.append(cafe_list[new_y][new_x])
                        cafe(new_x, new_y, flag, cnt + 1)
                        que.pop(-1)
                    else:
                        if start_x == new_x and start_y == new_y:
                            temp_ans = len(que)
                            if ans < temp_ans:
                                ans = temp_ans


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    cafe_list = [list(map(int, input().split())) for _ in range(N)]
    dy = [1, 1, -1, -1]
    dx = [-1, 1, 1, -1]
    ans = -1
    for a in range(N):
        for b in range(N):
            que = [cafe_list[b][a]]
            flag = 0
            start_x, start_y = a, b
            cafe(a, b, 0, 0)
    print(ans)
