"""
https://www.cut-the-knot.org/arithmetic/combinatorics/FibonacciTilings.shtml
규칙성 -> 점화식 -> DP
이전의 연산 결과가 다음 연산의 결과를 도출하는데 중복되는 경우 이를 활용

1. 점화식 구하기 -> 규칙 찾아 내기
2. 이전에 풀었던 결과를 활용하여 다음 step의 문제 해결에 활용하기
"""
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    n = N // 10         # 10의 배수를 종이의 폭으로 나눔
    """
    가로 10 / 20은 계산된 값 활용 - 피보나치와 구조
    10 -> 1가지
    20 -> 3가지
    30 -> 5가지 
    40 -> 11가지 
    50 -> 21가지
    ...
    """
    papers = [1, 3]
    for i in range(2, n):   # i-2 + i-1 -> i (최종적으로 append되는 값)
        """
        점화식 -> f(n) = f(n-1) + f(n-2)*2
        """
        papers.append(papers[i-1] + 2*papers[i-2])
    ans = papers[-1]
    print('#{} {}'.format(tc, ans))