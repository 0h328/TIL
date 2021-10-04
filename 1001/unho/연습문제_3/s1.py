"""
연습 문제3. 2의 거듭제곱

2의 거듭 제곱을 반복과 재귀버전으로 구현하시오.
"""

# 반복
def power_of_two_iteration(k):
    result = 1

    for i in range(k):
        result *= 2
    
    return result

print(power_of_two_iteration(4)) # 16


# 재귀
def power_of_two_recursion(k):
    if k == 1:
        return 2

    return 2 * power_of_two_recursion(k-1)

print(power_of_two_recursion(4)) # 16