import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    for _ in range(M):                      # 실행시간 많아짐
        data.append(data.pop(0))

    print('#{} {}'.format(tc, data[0]))
    # print('#{} {}'.format(tc, data[M % N]))


