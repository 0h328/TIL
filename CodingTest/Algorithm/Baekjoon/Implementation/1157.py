import sys
sys.stdin = open('input.txt')

words = input().upper()
words_list = list(set(words))

ans = []
for word in words_list:
    cnt = words.count(word)
    ans.append(cnt)

if ans.count(max(ans)) > 1:
    print('?')
else:
    print(words_list[ans.index(max(ans))])

