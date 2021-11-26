import sys
sys.stdin = open('input.txt')

tc = int(input())

for t in range(1, tc + 1):
    N = int(input())        # 미로 크기
    maze = []
    result = 1
    maze.append('4' * (N + 2))
    for _ in range(N):
        maze.append('4' + input() + '4')    # 미로 정보 입력
    maze.append('4' * (N + 2))
    print(maze)
    stack = []
    visited = [([0] * (N + 2)) for _ in range (N + 2)]

    try:
        start = maze[-2].index('2')
        final = maze[1].index('3')

        r = N - 2
        c = start

        while r >= 1:
            if maze[r - 1][c] == '0':         # 상
                if (((maze[r + 1][c] == '1') or (maze[r + 1][c] == '4')) and \
                    ((maze[r][c + 1] == '1') or (maze[r][c + 1] == '4')) and \
                    ((maze[r][c - 1] == '1') or (maze[r][c - 1] == '4')))\
                        or visited[r - 1][c] == 1:
                    r, c = stack.pop()

                else:
                    visited[r - 1][c] = 1
                    stack.append((r - 1, c))
                    r -= 1

            elif maze[r][c + 1] == '0':       # 우
                if (((maze[r + 1][c] == '1') or (maze[r + 1][c] == '4')) and \
                    ((maze[r - 1][c] == '1') or (maze[r - 1][c] == '4')) and \
                    ((maze[r][c - 1] == '1') or (maze[r][c - 1] == '4')))\
                        or visited[r][c + 1] == 1:
                    r, c = stack.pop()

                else:
                    visited[r][c - 1] = 1
                    stack.append((r, c + 1))
                    c += 1

            elif maze[r + 1][c] == '0':       # 하
                if (((maze[r - 1][c] == '1') or (maze[r - 1][c] == '4')) and \
                    ((maze[r][c + 1] == '1') or (maze[r][c + 1] == '4')) and \
                    ((maze[r][c - 1] == '1') or (maze[r][c - 1] == '4')))\
                        or visited[r + 1][c] == 1:
                    r, c = stack.pop()

                else:
                    visited[r + 1][c] = 1
                    stack.append((r + 1, c))
                    r += 1

            elif maze[r][c - 1] == '0':       # 좌
                if (((maze[r + 1][c] == '1') or (maze[r + 1][c] == '4')) and \
                    ((maze[r][c + 1] == '1') or (maze[r][c + 1] == '4')) and \
                    ((maze[r - 1][c] == '1') or (maze[r - 1][c] == '4')))\
                        or visited[r][c - 1] == 1:
                    r, c = stack.pop()

                else:
                    visited[r][c - 1] = 1
                    stack.append((r, c - 1))
                    c -= 1

            if maze[r][c] == '3':
                result = 1
                break

            else:
                result = 0

    except ValueError:
        result = 0

    except IndexError:
        result = 0

    finally:
        print("#{} {}".format(t, result))