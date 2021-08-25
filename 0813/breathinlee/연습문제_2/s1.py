def solve(word):
    ret = ''
    for i in range(len(word)-1, -1, -1):
        ret += word[i]
    return ret

# 문자열을 거꾸로 뒤집기(반복문 & 슬라이싱)

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(word2) # sgnirts siht esreveR
print(word2[::-1])