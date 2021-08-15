def solve(word):
    if len(word) == 0:
        return ''
    return word[-1] + solve(word[:-1])


import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab