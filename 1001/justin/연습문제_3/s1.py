"""
연습 문제3. 2의 거듭제곱

2의 거듭 제곱을 반복과 재귀버전으로 구현하시오.
"""

# 반복
def power_of_two_iteration(k):
    i = 0
    power = 1

    while i < k:
        power *= 2                # power -> 2를 몇 번 곱할 지
        i += 1                    # k를 넘지 않는 숫자만큼 반복 (첫 번째부터 시작해서 k번째 까지를 생각)
    return power

print(power_of_two_iteration(4))

# 재귀
def power_of_two_recursion(k):
    if k == 0:
        return 1
    else:
        return 2 * power_of_two_recursion(k-1)

print(power_of_two_recursion(4))