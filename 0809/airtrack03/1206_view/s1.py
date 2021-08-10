# SWEA에서 경우 위 2줄 주석 처리
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    check_idx = [2, 1, -1, -2]
    checked = [0] * N
    ans = 0

    for i in range(2, N - 2):
        if checked[i] == 1:
            continue

        # 문제 조건에서 건물 최대 높이는 255이므로 256으로 gap 초기값 설정
        min_gap = 256
        # i+2, i+1, i-1, i-2 높이가 모두 i보다 낮은지 확인
        for num in check_idx:
            if data[i] > data[i + num]:
                checked[i + num] = 1
                gap = data[i] - data[i + num]
                if min_gap > gap:
                    min_gap = gap
            else:
                min_gap = 256
                break

        if min_gap != 256:
            ans += min_gap

    print("#{} {}".format(tc, ans))