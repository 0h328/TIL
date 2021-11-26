"""
연습 문제1. 팩토리얼 재귀 호출

팩토리얼을 재귀 호출로 구현하고 결과가 도출 되기까지의 함수 호출 과정을 자유롭게 표현해보세요!
"""

def fact(n):

    if n <= 1:
        return 1

    else:
        return n * fact(n-1)

print(fact(4)) # 24