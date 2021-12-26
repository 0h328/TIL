import sys
from itertools import combinations
sys.stdin = open('input.txt')

# 풀이1
N, M = map(int, input().split())
cards = list(map(int, input().split()))
cases = list(combinations(cards, 3))    # cards 내 각 요소들을 3개씩 조합
diff = M + 1    # M과 case의 합이 가장 작은 차이를 구해야하므로 M보다 1큰 수를 지정

for case in cases:                  # 모든 조합을 돌면서
    if sum(case) == M:              # case합이 M과 같으면
        print(M)                    # M을 출력
        exit()                      # 프로그램 강제 종료
    elif sum(case) <= M:            # case합이 M을 넘지 않으면서
        if M - sum(case) < diff:    # M과 case의 합의 차가 diff보다 작으면
            diff = M - sum(case)    # diff를 M - sum(case)로 갱신

print(M - diff)


# 풀이2
# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# max_val = 0                       # 카드 3장의 합을 M과 가장 가까이 하기 위해 0으로 지정
#
# for i in range(N):                # 0부터
#     for j in range(i+1, N):       # i+1부터
#         for k in range(j+1, N):   # j+1부터
#             sum_case = cards[i] + cards[j] + cards[k] # cards의 중복되지 않는 idx를 합해준다.
#             if sum_case <= M and max_val < sum_case:  # case합이 M을 넘지 않으면서 max_val이 case의 합보다 작으면
#                 max_val = sum_case    # max_val을 case의 합으로 갱신
#
# print(max_val)
