'''
16진수 1자리는 2진수 4자리로 표시된다.
N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
단, 2진수의 앞자리 0도 반드시 출력한다.
예를 들어 47FE라는 16진수를 2진수로 표시하면 다음과 같다.
0100011111111110
'''
# 1 2 3 4 5 6 7 8 9 A B C D E F

def make_binary(num_list):
    binary_num = ''
    for i in num_list:
        for j in range(3, -1, -1):  # 1000 / 100 / 10 / 1 비교!
            if i & (1 << j):
                binary_num += '1'
            else:
                binary_num += '0'

    return binary_num


import sys
sys.stdin = open('input.txt')

hexa_list = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}  # 알파벳은 그냥 만들어 줬음 ord해서 빼고 해도 될거 같네

T = int(input())

for tc in range(1, T + 1):
    N, hexadecimal = input().split()
    num_list = []

    for i in hexadecimal:
        if i.isdigit():                     # 숫자라면?
            num_list.append(int(i))         # 글자로 받아서 int
        else:
            # num_list.append(hexa_list[i])     # key : value
            num_list.append(ord(i) - 55)        # 아스키 코드

    print('#{} {}'.format(tc, make_binary(num_list)))