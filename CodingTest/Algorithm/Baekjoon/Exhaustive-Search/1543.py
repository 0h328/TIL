import sys
sys.stdin = open('input.txt')

doc = input()
word = input()

# 풀이1
i = 0
cnt = 0

while i < len(doc):             # i가 doc길이랑 같아지면 마지막idx를 넘음
    j = 0
    while j < len(word):
        if doc[i] != word[j]:   # 문서와 찾는 단어의 idx를 비교하는데 불일치하면
            i -= j              # doc의 idx에서 word의 idx를 빼줌
            j = -1              # -1을 한 이유는 처음 idx에서 단어를 못 찾은 경우 처음 idx를 맞춰 주기 위해
        i += 1                  # 계속 다음 idx를 넘어가면서 탐색
        j += 1                  # 못찾은 경우에는 처음 idx / 찾은 경우에는 그 다음 idx 일치여부 확인
        if i == len(doc):       # i가 doc길이와 같아지면 못찾았으므로 break로 탈출
            break

    if i != len(doc): # j = len(word)이면서, 해당 조건이면 마지막 idx가기 전에 doc 내 word를 찾음
        cnt += 1
    elif j == len(word) and i == len(doc):
        # j = len(word)인데, doc의 마지막 위치에서 word를 찾음
        # ex) doc = abcabcdefg / word = efg인 경우
        cnt += 1

print(cnt)

# 풀이2
# result = doc.count(word)
# print(result)