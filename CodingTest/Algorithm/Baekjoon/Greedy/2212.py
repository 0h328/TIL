import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split()))
sensor.sort()

ans = []
for i in range(N-1):
    ans.append(sensor[i+1] - sensor[i])

ans.sort()

print(sum(ans[:N-K]))