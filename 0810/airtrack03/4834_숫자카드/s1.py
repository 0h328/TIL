import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cnt = [0] * 10
    data = input()

    for i in range(N):
        cnt[int(data[i])] += 1

    max_num = 0
    max_cnt = 0
    for j in range(10):
        if cnt[j] >= max_cnt:   # cnt 같을 경우, 가장 큰 수 출력 위해 같은 경우까지 조건 포함
            max_num = j
            max_cnt = cnt[j]

    print('#{} {} {}'.format(tc, max_num, max_cnt))