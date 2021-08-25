def solve(word):
    my_str = list(word)

    for i in range(len(my_str)//2):
        # tmp = my_str[i]
        # my_str[i] = my_str[len(my_str)-1-i]
        # my_str[len(my_str) - 1 - i] = tmp
        my_str[i], my_str[len(my_str)-1-i] = my_str[len(my_str)-1-i], my_str[i]

    reversed_my_str = ''.join(my_str)
    return reversed_my_str


# 문자열을 거꾸로 뒤집기(반복문 & 슬라이싱)

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(word2) # sgnirts siht esreveR
print(word2[::-1])