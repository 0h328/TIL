def solve(word):
    a = []
    for i in word[::-1]:
        a.append(i)
    return ''.join(a)

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(word2) # sgnirts siht esreveR