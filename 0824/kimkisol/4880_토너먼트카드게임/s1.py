import sys

sys.stdin = open('input.txt')


def get_winner(a, b) -> '(idx, value)':  # 튜플형태 a(번호, 값), b(번호, 값)
    rsp = {1: 3, 2: 1, 3: 2}  # 가위바위보 키(승자), 값(패자)
    if rsp[b[1]] == a[1]:  # 키와 값이 일치하면 키가 승자
        return b  # 튜플형태로 반환
    else:
        return a


def Tournament(s):  # s: students약자
    # 그룹이 1명인 경우
    if len(s) == 1:
        return s[0]
    # 그룹이 2명인 경우
    if len(s) == 2:
        return get_winner(s[0], s[1])
    # 그룹 분할 후 토너먼트 진행
    return get_winner(Tournament(s[:(len(s) - 1) // 2 + 1]), Tournament(s[(len(s) - 1) // 2 + 1:]))


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    s = list(enumerate(list(map(int, input().split())), 1))  # (번호, 값) 튜플 값으로 리스트 구성
    print(s)
    print('#{} {}'.format(t, Tournament(s)[0]))  # 최종값이 튜플이기 때문에 튜플 안 idx(번호) 출력
