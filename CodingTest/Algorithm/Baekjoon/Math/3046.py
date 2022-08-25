import sys
sys.stdin = open('input.txt')

R1, S = map(int, input().split())
print(2*S - R1)