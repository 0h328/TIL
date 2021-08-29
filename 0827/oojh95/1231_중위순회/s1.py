import sys
sys.stdin = open('input.txt')

def in_order(n):
    if n:
        in_order(left[n])
        visited.append(data[n][1])
        in_order(right[n])

for tc in range(1, 11):
    N = int(input())
    data = [[0]]
    for i in range(N):
        data.append(list(input().split()))
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(2, 3):
            try:
                left[i] = int(data[i][j])
                right[i] = int(data[i][j+1])
            except:
                pass

    visited = []
    in_order(1)
    print('#{} '.format(tc), *visited, sep='')
