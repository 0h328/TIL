import sys
sys.stdin = open('input.txt')

N = int(input())
# 회의가 끝나야 다음 회의를 시작할 수 있음
# 종료 시각 우선 정렬 / 시작과 동시에 회의가 끝남 -> 시작 시각으로 정렬
info = sorted((list(map(int, input().split())) for _ in range(N)), key=lambda x: (x[1], x[0]))

cnt = 0
tmp = 0                 # 회의 시작(종료 시각)을 0으로 초기화
for s, e in info:
    if s >= tmp:        # 종료 시각보다 시작 시각이 크면
        cnt += 1        # 회의 가능 횟수 +1
        # print(s, e)
        tmp = e         # 종료 시각으로 갱신

print(cnt)