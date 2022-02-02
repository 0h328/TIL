import sys
sys.stdin = open('input.txt')

S = int(input())
N = 0
tmp = 0
for i in range(1, S+1): # 1부터 S까지
    tmp += i            # 더하면서
    N += 1              # 덧셈 횟수 +1
    if tmp > S:         # 주어진 수보다 커지면
        N -= 1          # 횟수 -1
        break

print(N)