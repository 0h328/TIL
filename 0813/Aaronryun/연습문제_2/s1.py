import sys

sys.stdin = open('input.txt')

def solve_for(word):
    result = ''
    for i in range(len(word)-1,-1,-1):
        result+=word[i]
    return result

def solve_slice(word):
    result = word[::-1]
    return result

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve_for(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(solve_slice(word2)) # sgnirts siht esreve