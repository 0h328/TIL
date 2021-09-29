# 성렬님 코드 참고
import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    word = [list(input()) for _ in range(N)]
    result = N * M

    for i in range(N - 2): # 힌색이 갈 수 있는 범위 뒤에 파랑, 빨강 최소 한개씩 위치
        for j in range(i + 1, N - 1): # 파란색이 갈 수 있는 범위 앞에 한개, 뒤에 한개 제외한 나머지
            cnt = 0
            for row in range(i + 1):
                for col in range(M):
                    if word[row][col] != 'W':
                        cnt += 1
            for row in range(i + 1, j + 1):
                for col in range(M):
                    if word[row][col] != 'B':
                        cnt += 1
            for row in range(j + 1, N):
                for col in range(M):
                    if word[row][col] != 'R':
                        cnt += 1
            if result > cnt:
                result = cnt
    print('#{} {}'.format(tc+1, result))

