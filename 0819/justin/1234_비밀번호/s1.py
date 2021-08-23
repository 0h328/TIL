import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N, nums = map(list, input().split())  # N: 비밀번호 길이 / nums: 비밀번호
    while True:
        for i in range(len(nums)-1):      # 가장 마지막 요소는 볼 필요 없음
            if nums[i] == nums[i+1]:      # 만약 같으면
                nums.pop(i)               # 2개 꺼내고
                nums.pop(i)
                break
        else:                             # 같지 않으면
            break                         # 종료

    ans = ''.join(map(str, nums))         # 현재 남아있는 숫자가 비밀번호
    print('#{} {}'.format(tc, ans))