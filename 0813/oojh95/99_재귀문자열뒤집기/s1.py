def solve(word):
    n = len(word)
    if n == 1:
        return word
    else:
        return word[-1] + solve(word[0: n - 1])
    pass

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab