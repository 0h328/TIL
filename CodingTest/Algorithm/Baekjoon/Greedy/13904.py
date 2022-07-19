import sys
sys.stdin = open('input.txt')

N = int(input())
hw = []
for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    hw.append((d, w))

hw.sort()
complete_hw = []
date = hw[-1][0]
answer = 0
while True:
    if date == 0:
        break
    while hw and hw[-1][0] >= date:
        complete_hw.append(hw.pop()[1])
    date -= 1
    if not complete_hw:
        continue
    complete_hw.sort()
    answer += complete_hw.pop()

print(answer)