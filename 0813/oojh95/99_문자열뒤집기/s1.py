def solve(word):
    N = len(word)
    # 1번 리스트에 뒤에서부터 문자열 불러와서 저장
    # result = []
    # for i in range(N - 1, -1 , -1):
    #     result.append(word[i])
    #
    # return ''.join(result)
    # 2번 리스트 변환 후 좌우 값 swap
    result = list(word)
    for i in range(N // 2):
        result[i], result[N - 1 - i] = result[N - 1 - i], result[i]
    return ''.join(result)

    pass

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(word2[::-1]) # sgnirts siht esreve