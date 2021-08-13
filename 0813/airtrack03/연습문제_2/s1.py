def solve(word):
    ans = ''
    for i in range(len(word)-1, -1, -1):
        ans += word[i]

    return ans

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(word2) # sgnirts siht esreve
print(word2[::-1])