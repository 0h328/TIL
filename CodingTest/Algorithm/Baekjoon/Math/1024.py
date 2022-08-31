import sys
sys.stdin = open('input.txt')

N, L = map(int, sys.stdin.readline().split())

# 식
# n = x + (x+1) + (x+2) + ... + (x+(l-1))
# n = (x * l) + (1부터 l - 1까지 합)
# n = (x * l) + t
# x = (n - t) / l

t = 0 # (1부터 l - 1까지 합)
x = -1 # 초기값
cnt = 0 # 길이

# 반복문을 통해 모든 길이를 확인
for i in range(L, 101):
    t = (i * i - i) / 2

    # n - t를 i로 나누었을 때 나머지가 0이 나와야 정수가 된다.
    # n - t를 i로 나누었을 때 0보다 크거나 같아야 음이 아닌 것이다.
    if (N - t) % i == 0 and (N - t) // i >= 0:
        x = (N - t) // i # 초기값
        cnt = i # 길이
        break

# 초기값이 -1이면 수열을 만들 수 없는 것
if x == -1:
    print(-1)
else:
    # 길이만큼 반복해 초기값 + k를 출력
    for k in range(cnt):
        print(int(x + k), end=" ")