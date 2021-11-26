import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

#카운팅정렬
T = int(input())

for t in range(1, T + 1):
    nums_len = int(input())
    nums = list(map(int, input().split()))
    cnt_nums = [0] * (max(nums)+1)
    new_nums = [0] * nums_len

    #nums 안의 숫자를 cnt_nums의 idx로 넣어 개수 세기
    for num in nums:
        cnt_nums[num] += 1

    #cnt_nums에 개수를 누적으로 만들기
    for i in range(1, len(cnt_nums)):
        cnt_nums[i] += cnt_nums[i - 1]

    #누적 개수 -1(이유 1: cnt_nums는 개수이기 때문에 1부터 시작해서 -1을 해줌, 이유 2: 숫자를 넣을 예정이기 때문)
    #nums의 숫자의 개수를 뒤에서부터 확인하며, 누적 개수를 idx로해서 new_nums 리스트에 넣기
    for num in nums:
        cnt_nums[num] -= 1
        new_nums[cnt_nums[num]] = num

    print('#{} '.format(t), end='')
    for num in new_nums:
        print(num, end=' ')
    print()
