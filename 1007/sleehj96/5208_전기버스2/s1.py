import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    batteries = list(map(int, input().split()))
    N = batteries.pop(0)

    ans = 0     # 교체 횟수 정답으로 출력

    i = N-1-1       # i는 인덱스, = N-1의 한칸 전 부터 앞으로 순회
    while i > 0:
        cnt = 1     # 기본값 1

        for idx in range(i, -1, -1):    # i부터 맨 처음까지
            if batteries[idx] >= cnt:   # 갈 수 있는 만큼의 배터리가 있으면
                point = idx             # 그 때 교체
            cnt += 1
        # 뒤에서 부터 순회하므로 가장 작은 값으로 point 저장

        if point > 0:       # 처음 충전한 건 교체로 치지 않아서 생략
            ans += 1        # 교체 횟수 +1
            # charged[point] = 1

        i = point - 1       # point의 한칸 전 부터 다시 순회

    print('#{0} {1}'.format(tc+1, ans))
    # break
