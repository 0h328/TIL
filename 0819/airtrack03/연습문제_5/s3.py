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