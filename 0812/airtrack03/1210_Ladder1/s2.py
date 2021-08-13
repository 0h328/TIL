import sys

sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    N = 100
    ans = 0
    # 위에서부터 하나씩 내려가면서 끝이 2인지 확인
    for i in range(N):
        x = i
        y = 0
        visited = [[0] * N for _ in range(N)]

        if ladder[y][x] == 1:
            while True:
                visited[y][x] = 1
                if x-1 >= 0 and ladder[y][x-1] == 1 and visited[y][x-1] == 0:
                    x -= 1
                    continue
                elif x+1 < N and ladder[y][x+1] == 1 and visited[y][x+1] == 0:
                    x += 1
                    continue
                else:
                    y += 1

                if y == 99:
                    break

            if ladder[y][x] == 2:
                ans = i
                break
        else:
            continue

    print('#{} {}'.format(tc, ans))

