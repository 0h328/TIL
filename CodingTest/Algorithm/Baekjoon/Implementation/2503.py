import sys
from itertools import permutations
sys.stdin = open('input.txt')

N = int(input())
# 서로 다른 숫자 3자리 수이므로 순열 사용
# (1,2,3)과 (1,2,3), (1,2,4)와 (1,2,3) 이런식으로 비교하기 위해
nums = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))


for _ in range(N):
    num, strike, ball = map(int, input().split())
    num = list(str(num)) # 각 자리 숫자를 인덱스로 나누어 리스트화 시키기위해 str
    cnt = 0              # 삭제 횟수를 세기 위한 변수
    for i in range(len(nums)):
        strike_cnt, ball_cnt = 0, 0 # strike와 ball 개수를 비교하기 위해
        i -= cnt                    # 리스트에서 삭제 후, 다시 해당 인덱스부터 찾기 위해
                                    # (1,2,3)이 i=0이고, remove이후엔 (1,2,4)가 i=0이됨. 지정안하면, i=1(1,2,5)부터 찾음

        for j in range(3):          # 3자리만 비교하면 되므로 range(3)
            if nums[i][j] == num[j]:    # 동일한 자리의 수가 같으면
                strike_cnt += 1         # strike 개수 +1
            elif num[j] in nums[i]:     # 3자리 수가 있으나, 다른 자리에 위치하면
                ball_cnt += 1           # ball 개수 +1

        # strike_cnt와 인풋받은 strike가 다르면
        if (strike_cnt != strike) or (ball_cnt != ball):
            nums.remove(nums[i])    # 가능성이 없는 3자리 수이므로 삭제.
            cnt += 1                # 삭제했으면 삭제 횟수 +1

print(len(nums))

