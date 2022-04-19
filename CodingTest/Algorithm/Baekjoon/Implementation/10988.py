import sys
sys.stdin = open('input.txt')

word = input()
is_palindrome = 1
for i in range(len(word)//2):
    if word[i] != word[len(word)-1-i]:
        is_palindrome = 0
        break

print(is_palindrome)


