import sys
sys.stdin = open('input.txt')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    section = []
    for i in range(N):
        section.append(list(map(int, input().split())))

    cnt = 0
    max = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            for m in range(M):
                for n in range(M):
                    cnt += section[i + m][j + n]
            if max < cnt:
                max = cnt
            cnt = 0
    print('#{} {}'.format(test_case, max))
