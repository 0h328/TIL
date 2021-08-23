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
print(fibo(50))
print(cnt)