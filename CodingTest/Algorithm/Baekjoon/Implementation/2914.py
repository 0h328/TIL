import sys
sys.stdin = open('input.txt')

a, b = map(int, input().split(" "))
print(a*(b-1)+1)