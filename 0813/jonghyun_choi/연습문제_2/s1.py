def solve(word):
    reverse_str = ''
    for i in word:
        reverse_str = i + reverse_str
    return reverse_str


import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()

word2 = word2[::-1]
print(word2) # sgnirts siht esreve