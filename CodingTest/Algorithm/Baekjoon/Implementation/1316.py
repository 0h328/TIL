'''
문자열
인풋받은 단어의 알파벳이 바뀌는 시점의 개수와
정렬했을때 단어의 알파벳이 바뀌는 시점의 개수가 같아야 한다.

ex)
그룹 단어인 경우,
input) ccabbbzzz 단어가 바뀌는 시점의 개수 : 3번 c->a / a->b / b->z
정렬후) abbbcczzz 단어가 바뀌는 시점의 개수 : 3번 a->b / b->c / c->z

아닌 경우,
input) aaabbbccb 단어가 바뀌는 시점의 개수 : 3번 a->b / b->c / c->b
정렬후) aaabbbbcc 단어가 바뀌는 시점의 개수 : 2번 a->b / b->c
'''
import sys
sys.stdin = open('input.txt')

N = int(input())

cnt = 0                                     # 그룹 단어의 개수 cnt
for _ in range(N):
    word = input()                          # input
    word_sort = sorted(word)                # input 정렬
    dif_cnt_1 = 0                           # input 단어 바뀌는 시점 cnt
    dif_cnt_2 = 0                           # 정렬 단어 바뀌는 시점 cnt
    for i in range(len(word)-1):            # 마지막 idx까지 확인해야하므로 -1
        if word[i] != word[i+1]:            # 단어가 바뀌는 시점(같지 않을 경우)
            dif_cnt_1 += 1
    for i in range(len(word_sort)-1):       # 마지막 idx까지 확인해야하므로 -1
        if word_sort[i] != word_sort[i+1]:  # 단어가 바뀌는 시점(같지 않을 경우)
            dif_cnt_2 += 1

    if dif_cnt_1 == dif_cnt_2:              # input 바뀌는 시점 = 정렬 바뀌는 시점
        cnt += 1                            # 그룹 단어의 개수 +1

print(cnt)

