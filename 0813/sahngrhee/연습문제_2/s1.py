def solve(word):
    my_str = ''
    for i in word:
        my_str = i + my_str

    return my_str

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
word2 = word2[::-1]
print(word2) # sgnirts siht esreveR
