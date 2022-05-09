import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, input().split())        # 10, 3
pos = list(map(int, input().split()))   # 2, 9, 5 수의 위치
nums = deque(range(1, N+1))             # [1, 2, ... , 9, 10]
cnt = 0 # 연산의 횟수를 출력할 cnt
for i in range(M):
    if nums.index(pos[i]) < len(nums) - nums.index(pos[i]): # 뽑아내려는 수의 위치가 앞쪽에 가까우면
        while True:
            if nums[0] == pos[i]:       # 뽑아내려는 수와 위치가 같으면
                nums.popleft()          # 바로 뽑고
                break                   # break
            else:                       # 위치가 다르면
                nums.append(nums[0])    # 왼쪽으로 한칸 이동시키기
                nums.popleft()
                cnt += 1                # 연산횟수 +1
    else:                               # 뽑아내려는 수의 위치가 뒤쪽에 가까우면
        while True:
            if nums[0] == pos[i]:       # 뽑아내려는 수와 위치가 같으면
                nums.popleft()          # 바로 뽑고
                break                   # break
            else:
                nums.appendleft(nums[-1])   # 오른쪾으로 한칸 이동시키기
                nums.pop()                  # 큐 왼쪽에 추가 / 큐 마지막 제거
                cnt += 1                    # 연산횟수 +1

print(cnt)
