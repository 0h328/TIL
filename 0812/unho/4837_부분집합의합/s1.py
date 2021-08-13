import sys
sys.stdin = open('input.txt')


test_case = int(input())

A = [i for i in range(1, 13)]

for tc in range(1, test_case+1):
    N, K = map(int, input().split())
    answer = 0

    for i in range(1<<len(A)):
        tmp = []
        for j in range(len(A)):
            if i & (1<<j):
                tmp.append(A[j])                    # 리스트에 추가
        if len(tmp) == N and sum(tmp) == K:         # 리스트 길이가 N 이고, 합이 K이면 answer 증가
            answer += 1

    print('#{} {}'.format(tc, answer))