def solve(word):
    if word == '':
        return word
    return word[-1] + solve(word[:len(word)-1])

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab