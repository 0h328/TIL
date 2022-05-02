import sys
sys.stdin = open('input.txt')

N = int(input())
words = []  # 'DOG', 'GOD', ..
for i in range(N):
    words.append(input())

sorted_words = []   # [['D', 'G', 'O'], ['D', 'G', 'O'], ..]
for i in range(N):
    sorted_words.append(sorted(words[i]))

check_words = []    # 첫번째 단어 길이 3, 두번째 3, 세번째 4, 네번째 4
for i in range(N):
    if len(sorted_words[i]) >= len(sorted_words[0]): # 첫번째 단어보다 길면 길이만큼 추가
        check_words.append(len(sorted_words[i]))
    else:   # 첫번째 단어보다 짧으면 첫번째 단어의 길이만큼 추가
        check_words.append(len(sorted_words[0]))
print(check_words)

for i in range(1, N):   # 첫번째 단어는 확인할 필요 없음
    for j in range(len(sorted_words[0])):   # ['D', 'G', 'O']
        for k in range(len(sorted_words[i])):   # ['D', 'G', 'O']
            if sorted_words[i][k] == sorted_words[0][j]:    # 단어 비교해서 같으면
                check_words[i] -= 1 # 길이 -1
                sorted_words[i][k] = '' # 해당 글자 공백으로
                break

ans = 0
for i in range(1, N):
    if check_words[i] <= 1:
        ans += 1

print(ans)
