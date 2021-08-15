def solve1(word):#반복문
    res = ''
    for c in word:
        res = c + res
    return res


def solve2(word):# slicing
    return word[::-1]

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve1(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(solve2(word2)) # sgnirts siht esreve