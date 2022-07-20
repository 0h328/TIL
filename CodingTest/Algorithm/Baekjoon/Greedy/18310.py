import sys
sys.stdin = open('input.txt')

N = int(input())
arr = sorted(list(map(int, input().split())))
print(arr[(N-1)//2])