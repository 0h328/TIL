import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
tmp=[]
for i in range(N):
    tmp.append(int(sys.stdin.readline()))
for i in sorted(tmp):
    print(i)