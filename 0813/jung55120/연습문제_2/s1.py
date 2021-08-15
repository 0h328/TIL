def solve(word):
    word = list(word)

    for i in range(len(word)//2):
        word[i], word[len(word)-1-i] = word[len(word)-1-i], word[i]

    result = ''.join(word)
    return result

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(solve(word2)) # sgnirts siht esreve
