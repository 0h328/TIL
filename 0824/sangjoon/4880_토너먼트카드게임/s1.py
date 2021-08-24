# 문제 푼 시간
# 풀이법: 분할 정복 사용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def check_wind(a, b):  # 승부계산 함수
    if a[1] - b[1] == 0:  # 무승부 일 경우, 인덱스가 낮은 순으로 출력
        if a[0] < b[0]:
            return a
        else:
            return b

    elif a[1] - b[1] == 1 or a[1] - b[1] == -2:  # 승리조건 탐색
        return a

    else:
        return b


def tounerment(lst: list):  # 분할정복
    if len(lst) == 1:  # 재귀 종료 조건
        return lst[0]
    else:  # 2명 이상일 경우 승자계산
        mid = (len(lst)) // 2
        l = tounerment(lst[:mid])
        r = tounerment(lst[mid:])

        return check_wind(l, r)


test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    tm = []

    for i, p in enumerate(lst, start=1):  # 토너먼트 참가자 인덱스 초기화
        tm.append((i, p))

    winner = tounerment(tm)  # 토너먼트 승자 계산
    print("#{} {}".format(test, winner[0]))