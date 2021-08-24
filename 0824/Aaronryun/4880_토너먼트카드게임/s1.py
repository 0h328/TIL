import sys
sys.stdin = open('input.txt')

# 1 가위 2  바위 3 보

def battle(left, right):  # 가위바위보 판별
    left_value, right_value = data[left - 1], data[right - 1]  # 인덱스를 맞춰줘야 한다.
    if left_value - right_value == -1 or left_value - right_value == 2:
        return right
    return left

def winner(start, end):  # 재귀로 줄여보자 1, len(data) //index +1

    if start == end:  # 왼쪽과 오른쪽을 하나 남을때까지 진행
        return start
    else:
        mid = (start + end) // 2
        left_side = winner(start, mid)  # data[:mid]
        right_side = winner(mid + 1, end)
        return battle(left_side, right_side)


for test in range(1, 1 + int(input())):
    N = int(input())
    data = list(map(int, input().split()))

    answer = winner(1, len(data))
    print('#{} {}'.format(test, answer))

# if left_value == right_value:
#     return left
# elif left_value == 1:
#     if right_value == 3:
#         return left
#     elif right_value == 2:
#         return right
# elif left_value == 2:
#     if right_value == 1:
#         return left
#     elif right_value == 3:
#         return right
# elif left_value == 3:
#     if right_value == 2:
#         return left
#     elif right_value == 1:
#         return right
# 왼사람 오른사람 1이나 2를 냄 1-2 = -1 , 1,3일때 3-1 = 2 오른쪽사람이 이기는거 무조건
