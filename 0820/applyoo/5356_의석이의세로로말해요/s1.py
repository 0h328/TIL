import sys
sys.stdin = open('input.txt')


T = int(input())
for test in range(T):
    arr = []
    result = ''

    for i in range(5):  # 입력을 2차원 리스트로 저장
        word = list(input())
        for i in range(15-len(word)):  # 빈 칸은 공백으로 채움
            word.append('')
        arr.append(word)

    for i in zip(*arr):  # 결과 형태로 변환
        result += ''.join(i)

    print('#{} {}'.format(test+1, result))
