import sys
sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc + 1):
    print("#{}".format(t), end=" ")
    result = 0
    N, H = map(int, input().split())
