import sys
sys.stdin = open('input.txt')

N = int(input())
A = sorted(tuple(map(int, input().split())), key=lambda x: x)   # 최소를 구해야하므로 오름차순 정렬
B = list(map(int, input().split())) # B는 재배열 안됨

ans = 0
for i in range(N):
    b = B.pop(B.index(max(B)))  # 가장 큰 값을 pop하면서
    ans += A[i] * b             # 정렬된 A의 값과 곱하면서 누적합

print(ans)