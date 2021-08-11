# 재진님 풀이
import sys

sys.stdin = open('input.txt')

for T in range(int(input())):
    # k=1회충전시 최대거리, n=종점, m=충전기 설치된 정류장 개수
    k, n, m = map(int, input().split())
    # 0, n 추가 이유는 아래에
    s_oil = [0] + list(map(int, input().split())) + [n]

    result = 0
    # 시작점부터, 종점까지 갈 수 있는지 체크
    for i, s in enumerate(s_oil[:-1]):
        if s + k < s_oil[i + 1]:  # 현재 충전소 위치에서 다음 충전소위치에 도달 가능 여부
            break
    else:
        # 최소 충전횟수
        now_pos = 0
        while now_pos < n:  # 현재 위치가 도착점보다 작을때까지만
            for i in range(k, 0, -1):  # 갈 수 있는 최대 거리부터 -1씩
                if now_pos + i in s_oil:
                    now_pos += i
                    result += 1
                    break
        result -= 1

    print('#{} {}'.format((T + 1), result))