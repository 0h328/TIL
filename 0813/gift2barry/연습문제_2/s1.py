import sys
sys.stdin = open('input.txt')

def solve(word):
    my_str = list(word)

    for i in range(len(my_str)//2):
        temp = my_str[i]
        my_str[i] = my_str[len(my_str)-1-i]
        my_str[len(my_str) - 1 - i] = temp
    rev_my_str = ''.join(my_str)

    # 파이썬스러운방법
    # my_str[i], my_str[len(my_str)-1-i] = my_str[len(my_str)-1-i], my_str[i]

    return rev_my_str

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(word2[::-1]) # sgnirts siht esreveR