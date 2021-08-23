import sys
sys.stdin = open('input.txt')

def solve():
    DP = [0, 1, 3, 5] + [0] * 27
    for i in range(4, 31):
        DP[i] = DP[i-1] + DP[i-2] * 2 # 점화식 찾는 게 너무 어렵다
    return DP[N//10]

T = int(input())
for t in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(t, solve()))