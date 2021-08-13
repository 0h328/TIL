# 3. reversed()

def solve(word):
    result = "".join(reversed(word))
    return result



import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(solve(word2)) # sgnirts siht esreve
