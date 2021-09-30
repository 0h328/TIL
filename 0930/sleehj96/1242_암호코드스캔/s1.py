# import sys
# sys.stdin = open('input.txt')
#
# def simplify_passcode(code: str, step: int):    # 11001100110011 -> 1010101
#     s_str = ''
#     for i in range(0, len(code), step):
#         s_str += str(code[i])
#     return s_str
#
# def int_to_binary(n: int):
#     ans = ''
#
#     while n > 0:
#         ans += str(n % 2)
#         n //= 2
#
#     return ans[::-1].zfill(4)
#     # pass
#
# def validation(code: list):
#     my_sum = 0
#     # odd_sum = 0
#     # even_sum = 0
#     for idx in range(8):
#         if (idx+1) & 1:
#             my_sum += code[idx] * 3
#             # odd_sum += code[idx]
#         else:
#             my_sum += code[idx]
#             # even_sum += code[idx]
#     if my_sum % 10:
#         return False
#     return True
#
#
# passcodes = [
#     '0001101',
#     '0011001',
#     '0010011',
#     '0111101',
#     '0100011',
#     '0110001',
#     '0101111',
#     '0111011',
#     '0110111',
#     '0001011',
# ]
#
# for tc in range(int(input())):
#     N, M = map(int, input().split())   # 세로, 가로
#     arrays = [input() for _ in range(N)]
#     ans = 99999
#
#     for array in arrays:
#         arrays_to_check = []
#         idx = 0
#         temp = ''
#         while idx < M:
#             # print(temp)
#             if array[idx] != '0':
#                 temp += array[idx]
#                 # arrays_to_check.append(array[idx-6:idx+1])
#             else:
#                 if temp != '':
#                     arrays_to_check.append(temp)
#                     temp = ''
#             idx += 1
#         print(arrays_to_check)
#
#         binaried_code = []
#         for array_to_check in arrays_to_check:
#             temp = ''
#             if array_to_check:
#                 for letter in array_to_check:
#                     temp += int_to_binary(int(letter, 16))
#             binaried_code.append(temp)
#
#         print(binaried_code)
#
#         for code in binaried_code:
#             binaried = []
#             step = len(code)//(7*8)
#
#             while code[-1] != '1':
#                 # temp = code[-1]
#                 code = code[-1:] + code[:-1]
#                 # print(code)
#
#                 # code.insert(0, code.pop())
#             # print(code)
#             idx = len(code) - 1
#             while idx >= 0:
#                 binaried.append(code[idx + 1 - 7 * step:idx + 1])
#                 idx += 1 - 7 * step - 1
#
#             # print('binaried: ', binaried)
#             passcode = []
#             for case in reversed(binaried):
#                 if case:
#                     passcode.append(passcodes.index(simplify_passcode(case, step)))
#
#             # print(passcode)
#             if len(passcode) == 8:
#                 if validation(passcode):
#                     t_sum = sum(passcode)
#                     if ans > t_sum:
#                         ans = t_sum
#
#     if ans == 99999:
#         ans = 0
#
#     print('#{} {}'.format(tc+1, ans))
#     break


# 혼자 도저히 힘들어서 반장님 코드를 가져왔습니다..
#1. sol
from math import gcd
import sys

sys.stdin = open('input.txt', 'r')

T = int(input().strip())


# 16진법 숫자를 키값으로 가지며, 이진법으로 변환된 숫자를 밸류값으로 가지는 딕셔너리 구성
binary_nums = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}
# 흰색과 파란색의 넓이비가 k : a : b : c라고 할 때,
# 가장 간단한 정수비로 나타낸 a : b : c에서 abc를 키값으로 하는 딕셔너리 구성
ratio = {
    '211': '0',
    '221': '1',
    '122': '2',
    '411': '3',
    '132': '4',
    '231': '5',
    '114': '6',
    '312': '7',
    '213': '8',
    '112': '9',
}


# 세 정수가 주어질 때, 가장 간단한 정수비로 약분해서 반환해주는 함수
def abbreviation(num1, num2, num3):
    g = min(gcd(num1, num2), gcd(num2, num3))
    return [num1//g, num2//g, num3//g]


# 한 줄의 입력이 주어질 때, 해당 줄의 암호를 해독해서 리스트 형태로 반환해주는 함수
def row_decode(line):
    n = len(line)
    decoded = ''
    decoded_list = []
    # a : b : c 넓이비를 0 : 0 : 0 으로 초기화
    a, b, c = 0, 0, 0
    for idx in range(1, n):
        # b가 0인 상태에서 '1'이 나왔다면, a를 증가시키고
        if line[idx] == '1' and b == 0:
            a += 1
        # a가 0이 아니고, c가 0인 상황에서 '0'을 만나면 b를 증가시키고
        elif line[idx] == '0' and a != 0 and c == 0:
            b += 1
        # b가 0이 아닌 상태에서 '1'을 만나면 c를 증가시킨다.
        elif line[idx] == '1' and b != 0:
            c += 1
        # 만약 위의 경우가 아닌데 '0'을 만나면
        elif line[idx] == '0':
            # '0'이 나온 앞 자리가 '1'인 경우 하나의 코드가 종료되었다는 뜻
            if line[idx - 1] == '1':
                # a, b, c를 가장 간단한 정수비로 표현하여, decoded에 한 숫자씩 추가
                r = abbreviation(a, b, c)
                decoded += ratio[''.join(map(str, r))]
                # 다음 디코딩을 위해 a, b, c를 0으로 다시 초기화
                a, b, c = 0, 0, 0
                # 만약 해독문이 8글자일 경우
                if len(decoded) == 8:
                    # 해독문 리스트에 해당 해독문을 추가해주고, 다시 해독문을 빈 문자열로 초기화
                    decoded_list.append(decoded)
                    decoded = ''

    return decoded_list


# 입력된 코드가 유효한 코드인지 판별하는 함수
def is_valid(code):
    odd = [int(code[0]), int(code[2]), int(code[4]), int(code[6])]
    even = [int(code[1]), int(code[3]), int(code[5])]
    check = int(code[7])
    check_num = sum(odd) * 3 + sum(even) + check

    if check_num % 10 == 0:
        return True
    else:
        return False


for tc in range(1, T + 1):
    N, M = map(int, input().rstrip().split())  # N: 세로, M: 가로
    new = []
    # 입력받은 암호를 이진수로 변환해서 new 배열에 저장해주는 과정
    for _ in range(N):
        row = input().rstrip()
        temp = ''
        for i in range(M):
            temp += binary_nums[row[i]]
        new.append(temp)

    # 유효한 해독문을 중복 없이 저장해줄 set
    answer_set = set()

    # 2진수로 표현된 배열 new의 모든 줄에 대해서
    for i in range(N):
        # 해당 줄을 해독하여
        tmp = row_decode(new[i])
        # 해독문 목록 내의 해독문 t에 대해서
        for t in tmp:
            # t가 빈 문자열이 아니고
            if len(t) != 0:
                # 해독문 t가 유효할 경우에 set에 추가
                if is_valid(t):
                    answer_set.add(t)

    # 정답을 0으로 초기화하고,
    answer = 0
    # 가능한 해독문들에 대해서
    for x in answer_set:
        # 모든 해독문의 각 글자의 합을 answer에 더함
        for y in range(8):
            answer += int(x[y])

    print('#{} {}'.format(tc, answer))