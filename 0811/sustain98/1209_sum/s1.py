import sys
sys.stdin = open('input.txt')

for _ in range(10):
    idx = input()
    l = [list(map(int, input().split())) for _ in range(100)]

    max_sum = max(map(sum, l))                          # 행의 합 중 최댓값
    right_down = 0
    right_up = 0
    for i in range(100):
        right_down += l[i][i]                           #우하향 대각선의 합을 누적
        right_up += l[i][i]                             #우상향 대각선의 합을 누적
        tmp = 0
        for j in range(100):
            tmp += l[j][i]
        if max_sum < tmp:
            max_sum = tmp
    max_sum = max(max_sum, right_down,right_up)         #대각선들의 합과 행/열들이 합의 최대중 가장 큰 값을 max_sum에 할당
    print('#{} {}'.format(idx,max_sum))