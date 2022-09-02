from math import gcd
import sys
sys.stdin = open('input.txt')

N, S = map(int, input().split())
t = list(map(int, input().split()))
g = abs(t[0]-S)
# 수빈이의 위치와 동생의 위치 차이의 최대공약수를 구해야함.
for i in t[1:]:
    g = gcd(abs(i-S), g)

print(g)