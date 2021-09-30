import sys
sys.stdin = open('input.txt')

'''
(홀수자리합*3) + 짝수자리합 + 검증코드 % 10 == 0
하나의 배열에 1개의 암호코드가 존재
검증코드 확인해 정상적인 암호코드인지 판단
암호코드에 적혀있는 숫자들의 합 출력
'''

sheet = [
    '0001101', #0
    '0011001', #1
    '0010011', #2
    '0111101', #3
    '0100011', #4
    '0110001',
    '0101111',
    '0111011',
    '0110111',
    '0001011',
]

# 1. 암호 10진수로 변환
def convert(code):
    for i in range(8):
        temp = code[i*7:(i+1)*7]
        codenum.append(sheet.index(temp))

# 2. 암호 검증
def verify(codenum): # 입력 list으로 받아오기
    odd = 0
    even = 0
    for i in range(7):
        if not i % 2: # index가 짝수이면 홀수번째 숫자
            odd += codenum[i]
        else:
            even += codenum[i]
    if (odd * 3 + even + codenum[7]) % 10 == 0:
        return odd + even + codenum[7]
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    codenum = []

    for i in range(N):
        if '1' not in arr[i]:
            continue
        else:
            for j in range(M-1, -1, -1): # 뒤에서부터 1 찾기
                if arr[i][j] == '1': # 그때의 j가 맨 뒷 index
                    code = arr[i][j-55:j+1]
                    break
            break

    convert(code)
    print('#{} {}'.format(t, verify(codenum)))