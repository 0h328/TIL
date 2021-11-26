import sys

sys.stdin = open('input.txt')


def charge(p):
    global max_p, res
    idx = p  # 다음 충전소 위치를 저장할 변수
    for i in range(1, charges[p] + 1):  # 해당 충전소의 충전 용량 범위 (1~)
        if p + i >= N:  # POINT) 인덱스 범위 조건이 있어야 함
            res += 1  # 넘어갈 위치의 충전 카운트
            return
        temp_p = p + i + charges[p + i]  # 만약 p+i로 갔을때 최대한 이동할 수 있는 곳(현재 위치 + 이동칸수 + 이동한곳에서 최대 움직일 수 있는 칸수)
        if temp_p > max_p:
            max_p = temp_p
            idx = p + i  # POINT) 다음에 넘길 충전소를 갱신해나가야 함 (p+i는 현재 위치로부터 충전 용량 범위 내 떨어진 위치)
    res += 1  # 넘어갈 위치의 충전 카운트
    if max_p >= N:  # 넘어갈 위치에서 최대 이동 위치가 N을 넘어가면 더 볼 필요 없음
        return
    charge(idx)

T = int(input())

for t in range(1, T + 1):
    charges = [0] + list(map(int, input().split())) + [0]  # 충전소(문제랑 똑같이 구현하기 위해 0두개 추가)
    N = charges.pop(1)  # N값은 pop으로 따로 빼줌
    max_p = 1  # 갈 수 있는 최대 위치
    res = 0  # 충전 횟수

    charge(1)

    print('#{} {}'.format(t, res))