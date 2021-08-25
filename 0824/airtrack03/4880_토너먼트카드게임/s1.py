import sys
sys.stdin = open('input.txt')

def winner_check(data):
    # 1 가위 2 바위 3 보 => 이기는 경우: 차이 1 or -2
    if len(data) == 1:
        return data
    elif len(data) == 2:
        if data[1][1] - data[0][1] == 1 or data[1][1] - data[0][1] == -2:   # data[1]이 이기는 경우
            return [data[1]]
        else:   # 비기거나 data[0]이 이기는 경우
            return [data[0]]
    # 3명 이상인 경우
    length = len(data) - 1  # 문제에서 마지막 인덱스 j를 기준으로 나누므로
    left = data[:length//2 + 1]
    right = data[length//2 + 1:]

    return winner_check(winner_check(left) + winner_check(right))   # return 없으면 None Type 반환되어서 정답 X

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    data = [[idx+1, val] for idx, val in enumerate(temp)]   # 딕셔너리의 경우 인덱스로 접근 불가하기에 이중 리스트로 구현
    # , start = 1로 하면 idx + 1로 안 해도 됨

    ans = winner_check(data)[0][0]
    print('#{} {}'.format(tc, ans))