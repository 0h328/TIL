import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 컨테이너, M: 트럭
    w = list(map(int, input().split()))     # 컨테이너의 무게
    t = list(map(int, input().split()))     # 트럭의 적재용량
    w.sort(reverse=True)                    # 역순으로 정렬
    t.sort(reverse=True)
    c = ans = 0
    for i in range(M):                      # 컨테이너를 실을 수 있는 트럭의 수만큼 반복
        while c < N and w[c] > t[i]:        # 컨테이너 c가(무게) 트럭의 i(무게)보다 적재용량이 큰 경우
            c += 1                          # 다음 컨테이너 비교
        if c < N:
            ans += w[c]                     # 적재용량 이내면 운반(누적)
            c += 1
        else:                               # 아니면 종료
            break
    print('#{} {}'.format(tc, ans))