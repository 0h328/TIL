import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_val = 10000000            # 최대 & 최소값을 설정 해놓고 진행
    max_val = 0

    for i in range(N-M+1):        # N-M+1 구간합 (자주 사용됨)
        total = 0
        for j in range(M):        # M(구간) 만큼
            total += numbers[i+j] # 값을 합하고

        # print(total) # 쪼개지는 구간의 합
        if total < min_val: # 최대 & 최소 갱신 (이때 if & elif가 아닌 이유는?!)
            min_val = total
        if total > max_val:
            max_val = total

    result = max_val - min_val
    print('#{} {}'.format(tc, result))