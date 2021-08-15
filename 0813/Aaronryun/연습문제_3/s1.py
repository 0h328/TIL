import sys

sys.stdin = open('input.txt')

def solve(word):
    result = ''
    if len(word) == 1:
        result += word[0]
    elif len(word) == 0:
        return False
    else:
        result =  word[-1] + solve(word[:-1])
    return result

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab