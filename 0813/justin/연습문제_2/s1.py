def solve(word):
    my_str = list(word)

    for i in range(len(my_str)//2):
        #1. general
        # tmp = my_str[i]
        # my_str[i] = my_str[len(my_str)-1-i]
        # my_str[len(my_str)-1-i] = tmp

        #2. pythonic
        my_str[i], my_str[len(my_str)-1-i] = my_str[len(my_str)-1-i], my_str[i]

    reversed_my_str = ''.join(my_str)
    return reversed_my_str


import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
tmp = word2[::-1]
print(tmp) # sgnirts siht esreveR
