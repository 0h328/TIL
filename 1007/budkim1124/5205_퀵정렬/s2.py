import sys
sys.stdin = open("input.txt")


T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
