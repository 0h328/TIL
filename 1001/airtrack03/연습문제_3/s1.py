"""
연습 문제3. 2의 거듭제곱

2의 거듭 제곱을 반복과 재귀버전으로 구현하시오.
"""

# 반복
def power_of_two_iteration(k):
    result = 1
    while k > 0:
        result *= 2
        k -= 1
    return result

print(power_of_two_iteration(4)) # 16


# 재귀
def power_of_two_recursion(result, k):
    if k == 0:
        return result
    else:
        result *= 2
        return power_of_two_recursion(result, k - 1)

print(power_of_two_recursion(1, 4)) # 16