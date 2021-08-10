import sys

sys.stdin = open("input.txt")

num1 = int(input())
lst1 = map(int, input().split())

num2 = int(input())
lst2 = [list(map(int, input().split())) for _ in range(n)]
