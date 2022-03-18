import sys
sys.stdin = open('input.txt')

s = list(input())
tag = False
word = ''
res = ''
for i in s:
    if tag == False:
        if i == '<':
            tag = True
            word = word + i
        elif i == ' ':
            word = word + i
            res = res + word
            word = ''
        else:
            word = i + word

    elif tag == True:
        word = word + i
        if i == '>':
            tag = False
            res = res + word
            word = ''

print(res+word)

