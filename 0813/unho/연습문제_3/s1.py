def solve(word):
    #Base Case
    if len(word) == 1:
        return word[0]

    return word[-1] + solve(word[:-1])


    pass

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab