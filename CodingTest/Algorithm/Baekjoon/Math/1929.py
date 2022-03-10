import sys
sys.stdin = open('input.txt')

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N+1):
    if i == 1:
        continue
    for j in range(2, int(i**0.5)+1):   # 2부터 i의 제곱근까지 검사하면 나머지는 검사하나마나임
        if i % j == 0:
            break
    else:
        print(i)