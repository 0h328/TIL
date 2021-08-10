#sol1
import sys
sys.stdin = open('input.txt')

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))

    maxi = 0                            # num_list내 각 요소의 범위가 1이상 10000이하이므로
    mini = 10000*m                      # 구간합은 0보다 작을 수 없고, 10000*m보다 클 수 없다.

    for i in range(m, n+1):             # 0~m-1의 구간합을 시작으로 순차적으로 각 구간합을 확인
        x = sum(num_list[i-m:i])        # 구간합을 계산
        if x > maxi:
            maxi = x
        if x < mini:
            mini = x

    print('#{} {}'.format(idx, maxi-mini))



##2. sol
# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
#
# for idx in range(1, T+1):
#     N, M = map(int, input().split())
#     numbers = list(map(int, input().split()))
#                                                                 # 완전 탐색
#     results = []                                                # 구간합 값을 모두 추가해 줄 배열
#     for i in range(N - M + 1):                                  # index를 초과하지 않는 범위 고려
#         tmp = 0                                                 # 구간합을 넣어줄 임시 변수
#         for j in range(i, i + M):                               # 구간 합계를 구하기 위한 반복문
#             tmp += numbers[j]
#         results.append(tmp)                                     # 배열에 추가
#
#     print('#{} {}'.format(idx, max(results) - min(results)))


# 구간합을 가각ㄱ 구하지 말고 연속적인 구간들의 합을 비교할꺼니까
# 서로 포함 제외되는 값들을 비교해서 생각해볼 수도 있을것
