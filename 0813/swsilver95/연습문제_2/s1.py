def solve(word):
    new_word = ''
    for i in range(len(word) - 1, -1, -1):
        new_word += word[i]
    return new_word

import sys

sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
word2 = word2[::-1]
print(word2) # sgnirts siht esreveR