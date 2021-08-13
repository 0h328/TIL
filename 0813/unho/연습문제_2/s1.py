def solve(word):
    answer = ''
    for c in word:
        answer = c + answer
    return answer

def solve2(word):
    return word[::-1]

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(solve2(word2)) # sgnirts siht esreve