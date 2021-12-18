import sys
sys.stdin = open('input.txt')

word = input()
word_list = []
for i in range(len(word)):
    word_list.append(word[i:])

word_list.sort()    # 사전 순으로
for res in word_list:
    print(res)