import sys
sys.stdin = open('input.txt')

for case in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    res = 0
    for j in range(N):
        stack = []
        for i in range(N):
            if data[i][j] == 1:
                stack.append(data[i][j])
            elif data[i][j] == 2:
                if stack:
                    stack.clear()
                    res += 1

    print('#{} {}'.format(case + 1, res))

