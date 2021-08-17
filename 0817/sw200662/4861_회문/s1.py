import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    words = []
    ans = ''
    for k in range(N): # 하나의 리스트로받아옴 > 이유 string자체가 순회가 가능하므로, 이차원 배열처럼 쓸 예정
        words.append(input())
    #print(words)
    for z in words:  # 먼저 가로
        for k in range(N - M + 1):
            cnt = 0
            while cnt <= (M // 2 - 1):
                if z[k + cnt] != z[k + M - 1 - cnt]: # 길의만큼의 양끝비교, 틀리다면 break로 나와버림
                    break
                if cnt == M // 2 - 1: # 만약 while문의 끝점까지도착(가운데 값까지 도착) 한다면
                    for l in range(M): # 시작점부터 그 word를 찾아가면서 더해줌
                        ans += z[k + l]
                cnt += 1 # while문의 cnt값을 증가

    for length in range(N):  # 그다음 세로
        for width in range(N - M + 1):
            cnt = 0
            while cnt <= (M // 2 - 1):
                if words[width + cnt][length] != words[width + M - 1 - cnt][length]:
                    break
                if cnt == M // 2 - 1:
                    for f in range(M):
                        ans += words[width + f][length]
                cnt += 1
    print('#{} {}'.format(i + 1, ans))
