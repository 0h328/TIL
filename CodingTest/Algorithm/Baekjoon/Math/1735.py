import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())
C, D = map(int, input().split())

# 최대공약수를 구하는 코드
def gcd(x, y):
    if y == 0:
        return x
    x, y = y, x % y
    return gcd(x, y)

child = A * D + C * B
parent = B * D

common = gcd(max(child, parent), min(child, parent))

print(child//common, parent//common)


