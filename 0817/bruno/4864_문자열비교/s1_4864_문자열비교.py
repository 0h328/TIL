import sys
sys.stdin = open('input.txt')

T = int(input())
# for tc in range(1, T+1):
#     word = input()
#     target = input()
#     cnt = 0
#
#     for i in range(len(target) - len(word) + 1):
#         if target[i:i+len(word)] == word:
#             cnt = 1
#             break
#     print('#{} {}'.format(tc, cnt))

def is_included(target, search):
    for i in range(len(target) - len(search) + 1):
        for j in range(len(search)):
            if target[i + j] != search[j]:
                break
        else:
            return 1
    return 0

for t in range(1, T+1):
    search = input()
    target = input()
    print('#{} {}'.format(t, is_included(target, search)))