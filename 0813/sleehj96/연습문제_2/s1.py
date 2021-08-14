import sys


def solve(word):
    ans_word = ''
    for idx in range(len(word)-1, -1, -1):
        ans_word += word[idx]
    return ans_word


sys.stdin = open('input.txt')

# 1. 반복문 활용
word = input()
print(solve(word)) # edcba

# 2. pythonic (slicing)
word2 = input()
print(word2[::-1]) # sgnirts siht esreve