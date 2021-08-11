import sys

sys.stdin = open('input.txt')

data = list(map(int, input().split()))
N = len(data)

for i in range(1 << N):			# 1 << N : 부분 집합의 개수
    for j in range(N):			# 원소의 수만큼 비트를 비교
        if i & (1 << j):			# i의 j번째 비트가 1이면 j번째 원소 출력
            print(data[j], end=' ')
    print()
print()