import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, C = input().split()
    num = []
    for i in N:
        num.append(int(i))
    m = max(num)
    idx = N.find(str(m))
    