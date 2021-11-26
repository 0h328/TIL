import sys
sys.stdin = open('input.txt')

tc = int(input())

for tt in range(1, tc + 1):
    result = 0  # 결과값
    N, M = map(int, input().split())        # 컨테이너 수, 트럭 수
    W = list(map(int, input().split()))     # 화물의 무게
    T = list(map(int, input().split()))     # 트럭의 적재 용량
    for t in T:
        max_w = 0               # 트럭이 실을 수 있는 최대 화물 무게
        for w in W:
            if w <= t:          # 현재 트럭 무게보다 작은 화물이면
                if max_w < w:   # 현재 최대 화물 무게보다 클 시
                    max_w = w   # max_w 갱신
        if max_w in W:          # 없으면 remove에서 에러나므로 W에 존재할 시
            W.remove(max_w)     # W에서 제외
            result += max_w     # 결과값에 max_w 더해줌

    print("#{} {}".format(tt, result))