import sys
sys.stdin = open('input.txt')

N = int(input())
R = 0

for _ in range(N):
    if int(input()) == 1:
        R += 1

if R > N//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")