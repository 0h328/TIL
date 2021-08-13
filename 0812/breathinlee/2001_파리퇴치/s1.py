import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # arr[i][j] + arr[i+1][j+1] + arr[i][j+1] + arr[i+1][j+1]
            m_square_sum = 0
            for k in range(M):
                for t in range(M):
                    m_square_sum += arr[i+k][j+t]
            #print(m_square_sum)
            if m_square_sum > max_sum:
                max_sum = m_square_sum
    print('#{} {}'.format(tc, max_sum))