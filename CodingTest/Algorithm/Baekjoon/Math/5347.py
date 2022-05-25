import sys
sys.stdin = open('input.txt')

n = int(input())

# 최소 공배수 구하는 함수
def lcm(a, b):
    return (a * b) // gcd(a, b) # 두 수의 곱에서 최대 공약수를 나눈다.

# 최대 공약수 구하는 함수
def gcd(a, b):
    if b % a:
        return gcd(b % a, a)
    else:
        return a

for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))
