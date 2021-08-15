def solve(word):
    result = ''

    def my_reverse(word):
        nonlocal result
        if len(word) == 1:
            result += word
        else:
            result += word[-1]
            my_reverse(word[:len(word)-1])

    my_reverse(word)
    return result

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab