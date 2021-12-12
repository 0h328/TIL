'''
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
'''

# import sys
# sys.stdin = open('input.txt')
#
# N = int(input())
#
# word_set = set()
# for _ in range(N):
#     word_set.add(sys.stdin.readline().strip())
#
# word_list = list(word_set)
# # 앞에 x: len(x) 각 요소(x)를 길이로 먼저 정렬, x: x 각 요소(x)를 사전으로 정렬
# word_list.sort(key=lambda x : (len(x), x), reverse=True)
#
# while word_list:
#     print(word_list.pop())

import sys
sys.stdin = open('input.txt')

N = int(input())

word_list = []
for _ in range(N):
    # sys.stdin.readline은 '\n'이 기본값이므로, strip을 통해 제거해줘야함.
    word_list.append(sys.stdin.readline().strip())

word_set = set(word_list)               # 중복문자 제거 (set)
word_list = list(word_set)              # 중복문자 제거 후 list화
word_list.sort()                        # 사전순서로 정렬
word_list.sort(key=lambda x: len(x))    # 길이순서로 정렬

for word in word_list:
    print(word)

