import sys
sys.stdin = open('input.txt')

ch = [1, 1, 2, 2, 2, 8]
info = list(map(int, input().split()))
for i in range(6):
    print(ch[i]-info[i], end=' ')