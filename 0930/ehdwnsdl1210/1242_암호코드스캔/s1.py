'''
1. 총 8개의 숫자로 이루어져 있다.
2. 앞 7자리는 상품 고유의 번호를 나타내며, 마지막 자리는 검증 코드를 나타낸다.

1. 세로 2000. 가로 500 이하의 크기를 가진 직사각형 배열에 암호코드 정보가 포함되어 전달,
하나의 배열에는 1개 이상의 암호코드가 존재한다.
(단, 모든 암호코드가 정상적인 암호코드임을 보장할 수 없다. 비정상적인 암호코드가 포함될 수 있다.)
2. 배열은 16진수로, 이 배열을 2진수로 변환하여 그 안에 포함되어 있는 암호코드 정보를 확인한다.
3. 정상적인 암호코드들을 판별한 뒤 이 암호코드들에 적혀있는 숫자들의 합을 출력한다.

1. 암호코드들이 붙어있는 경우는 존재하지 않는다.
(각 암호코드의 둘레에는 최소 1칸 이상의 빈 공간이 존재한다.)
2. 암호코드가 일부만 표시된 경우는 없다. 모든 암호코드는 8개의 숫자로 구성되어 있다.
3. 암호코드의 가로 길이는 암호코드 선의 두께에 따라 달라지며,
두께가 가장 가는 경우, 숫자 하나가 차지하는 길이는 7칸
4. 암호코드 하나의 최소 가로 길이는 56이며,
암호코드 선이 굵어질 경우, 56의 배수의 길이
예를 들어 암호코드 숫자 하나가 14칸을 사용하는 경우, 암호코드 하나의 가로길이는 112
암호코드 하나에 포함되는 암호코드 숫자들은 모두 동일한 크기를 갖는다.
'''

from pandas import DataFrame

import sys
sys.stdin = open('input.txt')

# # 암호코드를 통째로 만들기
# code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]
# code[0][0][0][1][1][0][1] = 0
# code[0][0][1][1][0][0][1] = 1
# code[0][0][1][0][0][1][1] = 2
# code[0][1][1][1][1][0][1] = 3
# code[0][1][0][0][0][1][1] = 4
# code[0][1][1][0][0][0][1] = 5
# code[0][1][0][1][1][1][1] = 6
# code[0][1][1][1][0][1][1] = 7
# code[0][1][1][0][1][1][1] = 8
# code[0][0][0][1][0][1][1] = 9
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = [list(map(str, input())) for _ in range(N)]
#     # print(DataFrame(arr))
#
#     # 1개인 경우는 하겠는데, 2개 이상이면 어떻게 찾지?!
#
#     find_code = []  # 해당 행 볼려고
#
#     hexa_list = []
#     for k in range(len(find_code) - 1, -1, -1):
#         while find_code[k] != 0:  # 암호코드 마지막이 무조건 0이아님
#             hexa_list.append(find_code[k])  # 거꾸로 담아짐(16진수가)
#
#     hexa_num = ''
#     for i in hexa_list[::-1]:
#         if i.isdigit():             # isdigit()이면 그대로
#             hexa_num += i           # 아니면 ord 쓰고
#         else:
#             hexa_num += str(ord(i) - 55)
#
#     # 찾고 난후에는 16 -> 2변환
#
#     # 나온숫자들을 range(3, -1, -1) 돌려서 >> 이걸로 찾아서 문자열로 일단 합체
#     # 1일 제일 끝이니까 거기서 시작하면 되고
#
#     # 선이 제일 얇을 때는 그냥 하면 되고
#
#     # 선이 굵어지면?! (56, 112, 168, 224, 280, 336, 392, 448)
#     # 찾는 인덱스를 배수하면될거 같고...

t1 = {'211': 0, '221': 1, '122': 2, '411': 3,
      '132': 4, '231': 5, '114': 6, '312': 7,
      '213': 8, '112': 9}
t2 = {}
for i in range(0, 16):  # 16진수 => 2진수 변환 딕셔너리 생성
    if i < 10: t2[str(i)] = '{0:0>4}'.format(str(bin(i))[2:])
    else: t2[chr(55+i)] = '{0:0>4}'.format(str(bin(i))[2:])

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input().rstrip() for _ in range(N)]
    # print(arr)

    binary = [''] * N
    for i in range(N):  # 16 => 2진수 변환
        for var in arr[i]:
            binary[i] += t2[var]

    ans = 0
    v, key = [], []
    for n in range(N):
        a = b = c = 0
        if '1' in binary[n]:  # 암호가 있는 경우
            for m in range(M*4-1,-1,-1):
                if b == 0 and c == 0 and binary[n][m] == '1':  # 맨 뒤의 1의 개수
                    a += 1
                elif a and c == 0 and binary[n][m] == '0':  # 1 다음 0의 개수
                    b += 1
                elif a and b and binary[n][m] == '1':  # 1, 0 다음의 1 개수
                    c += 1
                elif c and binary[n][m] == '0':  # 다시 0이 나온 경우
                    w = min(a, b, c)  # 최솟값(가중치)
                    key.append(t1[str(c//w) + str(b//w) + str(a//w)])  # 뒤의 3개 자리수만으로 판별
                    a = b = c = 0  # 0으로 초기화
                    if len(key) == 8:  # 암호 해독 시도가 가능한 경우
                        if key not in v:  # 반드시 37 line이랑 개행되어 있어야 함
                            if ((key[7]+key[5]+key[3]+key[1])*3 + key[0]+key[2]+key[4]+key[6]) % 10 == 0:  # 검증
                                ans += sum(key)
                            v.append(key)
                        key = []
    print('#{} {}'.format(test_case, ans))
