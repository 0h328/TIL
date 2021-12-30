import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

tmp = []

for i in range(2, N+1): # 2부터 N까지 모든 정수
    tmp.append(i)

p = tmp[0]              # 지우지 않은 수 중 가장 작은 수 P
j = 0                   # 배수의 크기를 구하기 위한 변수
cnt = 0                 # 지울때마다 count
while cnt < K:          # K번째를 넘어가면 종료
    j += 1
    cnt += 1
    if p*j in tmp:
        tmp.remove(p*j)
    elif p*j > max(tmp):
        p = tmp[0]
        j = 0
        cnt -= 1
    elif p*j not in tmp:
        cnt -= 1
        pass

print(p*j)



