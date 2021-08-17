def solve(word):
    word_l = list(word)
    for i in range(len(word_l)//2):
        word_l[i], word_l[-1-i] = word_l[-1-i], word_l[i]
    reverse_word = ''.join(word_l)
    return reverse_word

# def solve(word):
#     word = word[::-1]
#     return word

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(solve(word2)) # sgnirts siht esreveR
