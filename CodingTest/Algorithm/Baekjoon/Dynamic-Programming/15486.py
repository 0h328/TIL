import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
case = []   # idx 0은 상담일 수, idx 1은 금액
dp = [0] * (N+1)
check = 0

for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    case.append([t, p])

for i in range(N):
    check = max(check, dp[i])   # dp에 금액을 누적시켜 저장하고 계속 check로 갱신
    if case[i][0] + i <= N:     # 상담가능일이 퇴사예정일보다 작아야함
        # (해당 상담일 금액 + 누적된 상담 금액)과 현재 저장된 dp값 중 최대를 갱신
        dp[case[i][0] + i] = max(case[i][1]+check, dp[case[i][0] + i])

print(max(dp))