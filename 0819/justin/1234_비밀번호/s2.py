import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    _, nums = map(list, input().split())

    for _ in range(len(nums)):    # len(nums) - 1으로 설정해도 됨
        i = 0                     # i가 문자열 길이보다 1개 작은 구간
        while i < len(nums)-1:    # 마지막 인덱스 전까지 반복
            if nums[i] == nums[i+1]:    # 같으면
                del nums[i]             # 리스트에서 지우고
                del nums[i]
            else:                       # 다르면
                i += 1                  # 다음을 보자
    ans = ''.join(nums)
    print('#{} {}'.format(tc, ans))