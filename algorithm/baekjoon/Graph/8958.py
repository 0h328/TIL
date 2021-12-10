import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    quiz = input()

    score = 0
    cnt = 0
    for ox in quiz:
        if ox == 'O':
            cnt += 1
            score += 1 * cnt
        else:
            score += 0 * cnt
            cnt = 0

    print(score)

# T = int(input())
# for tc in range(1, T+1):
#     quiz = input().split('X')
#
#     score = 0
#     for correct in quiz:
#         score += len(correct) * (len(correct) + 1) // 2
#
#     print(score)