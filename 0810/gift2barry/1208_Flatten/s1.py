#총 소요시간 66:15

import sys
sys.stdin = open('input.txt')

# 치트키1
def init():
    # Test 케이스 횟수 10회
    T = 10
    for _ in range(1, T+1):

        # 인풋값들
        dumps = int(input())
        blocks = list(map(int, input().split()))

        # 덤프 횟수동안,
        for i in range(dumps):
            # block 정렬하고 가장 앞에값 +1, 가장 뒤에값-1 반복
            blocks.sort()
            blocks[0] += 1
            blocks[len(blocks)-1] -= 1

        # 덤프 횟수 소진하면 남은 리스트에서 (max - min) = 정답
        highest = max(blocks)
        lowest = min(blocks)
        ans = highest - lowest
        print('#{} {}'.format(_, ans))

init()



# 패작1
# def init():
#
#     #Test 케이스 횟수 10회
#     T = 10
#     for _ in range(T):
#         #input 값 들 불러오기
#         dump_num = int(input())
#         blocks = list(map(int, input().split()))
#
#         # dump 횟수만큼 max & min 확인
#         for cycle in range(dump_num):
#             # get index & value of max height
#             for i, high in enumerate(blocks):
#
#                 # if found the max height, decrease its height
#                 if high == max(blocks):
#                     blocks[i] -= 1
#
#                     # when max height found, increase min height
#                     for j, low in enumerate(blocks):
#                         if low == min(blocks):
#                             blocks[j] += 1
#
#         ans = max(blocks) - min(blocks)
#         print(ans)
#
# init()