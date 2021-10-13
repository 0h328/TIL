import sys
sys.stdin = open('input.txt')
#종현님 풀이 참고!
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
def dessert_tour(i, j, visited, start_point, cnt, k):
    global ans
    # if (i, j) not in visited and not desserts[cafes[i][j]]:
    #     visited.append((i, j))
    #     stack.append((i, j))
    #     desserts[cafes[i][j]] = 1
    if k > 3:
        return
    if (i, j) == start_point and cnt != 0:
        if ans < cnt:
            ans = cnt
        return

    #지나왔던 경로가 저장되는 코드!
    # for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]
    if 0 <= ni < N and 0 <= nj < N and cafes[ni][nj] not in visited:
        dessert_tour(ni, nj, visited+[cafes[ni][nj]], start_point, cnt + 1, k)
        dessert_tour(ni, nj, visited + [cafes[ni][nj]], start_point, cnt + 1, k+1)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(N):
        for j in range(N):
            dessert_tour(i, j, [], (i, j), 0, 0)

    print(ans)
