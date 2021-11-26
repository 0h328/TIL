def solve(word):

    # reverse_word = ''
    # for i in word:
    #     reverse_word = i + reverse_word
    #
    # return reverse_word

    my_str = list(word)
    for i in range(len(my_str)//2):
        tmp = my_str[i]
        my_str[i] = my_str[len(my_str)-1-i]
        my_str[len(my_str)-1-i] = tmp

    reversed_my_str = ''.join(my_str)
    return reversed_my_str

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
word2 = word2[::-1]
print(word2) # sgnirts siht esreve
