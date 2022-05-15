import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
stick = [int(sys.stdin.readline()) for _ in range(N)]
ans = 1             # 볼때 하나부터 보고 시작하므로 1
max_h = stick[-1]   # 맨 뒤꺼 먼저 봐야해서 인덱스 -1
for i in range(N-1, -1, -1):    # 뒤에서 두번째꺼 부터 순회
    if stick[i] > max_h:        # 맨 뒤보다 크면
        ans += 1                # 볼 수 있는 막대 +1
        max_h = stick[i]        # 갱신

print(ans)