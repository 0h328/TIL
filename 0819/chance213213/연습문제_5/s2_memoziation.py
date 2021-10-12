# 저장 공간을 만들어 놓은 상태에서 저장 (길이를 직접 지정)
def fibo(n):
    global cnt
    cnt += 1
    if memo[n] == -1:                   # 값을 아직 구하지 않은 경우
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1] * 51 # n의 크기보다 1 크게 생성
memo[0] = 0
memo[1] = 1
cnt = 0

# print(memo)
print(fibo(10))
print(cnt)


import time
start = time.time()

# 저장 공간을 만들어 놓은 상태에서 저장 (길이를 직접 지정)
def fibo2(n):
    global cnt
    cnt += 1
    if n >= 2 and memo2[n] == 0:        # 아직 계산되지 않은 값이면
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

memo2 = [0] * 51
memo2[0] = 0
memo2[1] = 1
cnt = 0

# print(memo)
print(fibo2(50))
print(cnt)