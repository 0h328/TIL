# https://www.cut-the-knot.org/arithmetic/combinatorics/FibonacciTilings.shtml

# * 아래 3가지 방식을 생각하는데 30분정도 소요
# 1. 문제가 DP로 푸는 방식인지 아닌지 먼저 파악하기
# 2. DP로 푸는 문제 같다? 그럼 1부터 규칙찾기
# 3. 규칙찾고 점화식 세우기

# N = 1 (1)
# N = 2 (3)
# N = 3 (5) (3 + 2*1)
# N = 4 (11) (5 + 2*3)

# 위에 3가지 방식 생각하기 전에는 2차원 리스트 만들 생각했음.
# 그래서 20xN의 넓이를 통해 인덱스 [0][0]과 [0][1] 곱해서 경우의 수 더하는 식으로 구하는 법 생각했음.
# 위와 같은 방식으론 절대 풀 수 없고, 분명 간단히 풀릴 거라고 생각해서 10분간 생각만함.

# fibo 및 pascal과 유사하여 첫번째와 두번째 idx는 애초에 설정하고 풀어도 된다라고 판단.
def put_a_paper(k):

    if k == 1:             # 첫번째 idx 10은 1
        return 1
    if k == 2:             # 두번째 idx 20은 1
        return 3

    return put_a_paper(k-1) + 2*put_a_paper(k-2)

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    k = N//10               # 10의 배수이기 때문에, 10으로 나눠서 풀이

    print("#{} {}".format(tc, put_a_paper(k)))