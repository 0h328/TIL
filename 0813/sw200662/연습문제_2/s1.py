def solve(word):
    newword = ''
    for i in range(len(word)):
        newword += word[len(word)-1-i]
    return newword


import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(word2[::-1]) # sgnirts siht esreve