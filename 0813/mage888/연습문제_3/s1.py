def solve(word):

    if len(word) == 1:
        return word
    else:
        return solve(word[1:]) + word[0]


import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab