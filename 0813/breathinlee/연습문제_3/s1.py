def solve(word):
    if len(word) < 1:
        return word
    return solve(word[1:]) + word[0]

# 문자열을 거꾸로 뒤집기(재귀함수)

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab
