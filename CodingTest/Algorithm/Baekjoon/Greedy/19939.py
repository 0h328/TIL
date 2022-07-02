import sys
sys.stdin = open('input.txt')

def solution():
    sum_minimum = K*(K+1)//2
    if sum_minimum > N:
        return -1
    if (N-sum_minimum) % K == 0:
        return K-1
    else:
        return K

N, K = map(int, input().split())

print(solution())