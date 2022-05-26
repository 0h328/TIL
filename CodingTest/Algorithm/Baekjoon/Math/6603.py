import sys
sys.stdin = open('input.txt')
from itertools import combinations

while True:
    nums = list(map(int, input().split()))

    for i in combinations(nums[1:], 6): # 6가지 수로 조합해서 반복
        print(*i)

    if nums[0] == 0:    # 첫번째 인덱스가 0이면
        exit()          # 종료
    print()             # 개행

