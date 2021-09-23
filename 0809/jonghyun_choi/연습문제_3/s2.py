# 복습
import sys
sys.stdin = open('input.txt')

# 90도 회전 시 낙차가 가장 큰 상자의 낙차를 구하려면?
# 회전 시 나와 같이 떨어지는 (회전 전 나와 같은 높이) 상자의 개수가 적으면 가장 낙차가 크게 떨어짐

T = int(input())

for case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    height = [0] * N
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                height[i] += 1
    max_height = height[0]
    for h in height:
        if h > max_height:
            max_height = h
    print('#{} {}'.format(case + 1, max_height))

