import sys


def solve(word, ans_word=''):

    if not word:
        return ans_word

    else:
        ans_word += word[-1]
        return solve(word[:-1], ans_word)


sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab