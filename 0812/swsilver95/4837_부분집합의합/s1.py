import sys

sys.stdin = open('input.txt')

numbers = list(range(1, 13))

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())

    tot_cnt = 0
    for i in range(1<<12):
        cnt = 0
        tmp = []
        for j in range(12):
            if i & (1<<j):
                tmp.append(numbers[j])
                cnt += 1
                if cnt > N:                 # 연산 수를 조금이라도 줄이기 위해 부분집합의 길이가 N을 초과하면 바로 취소
                    break
        else:
            if len(tmp) == N:               # 길이가 N과 같은 부분집합 중에서
                if sum(tmp) == K:           # 원소의 합이 K인 부분집합이 있다면
                    tot_cnt += 1            # 개수에 1을 더해줍니다.
    print('#{} {}'.format(tc, tot_cnt))