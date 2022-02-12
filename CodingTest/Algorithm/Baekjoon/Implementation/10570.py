import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    V = int(input())

    # 가장 작은 수를 출력하기 위해 내림차순 정렬
    nums = sorted(list(int(input()) for _ in range(V)), reverse=True)
    cnt = 0
    ans = 0

    for i in range(V):
        if nums.count(nums[i]) >= cnt:  # 숫자의 개수가 cnt보다 크거나 같으면
            cnt = nums.count(nums[i])   # cnt는 숫자의 개수로 갱신
            ans = nums[i]

    print(ans)

