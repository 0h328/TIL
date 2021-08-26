
def enQueue(item):
    global rear
    rear += 1
    rear = rear % len(nums)
    nums[rear] = item


def deQueue():
    global front
    front += 1
    front = front % len(nums)
    change_num = nums[front]
    nums[front] = 0
    return change_num

import sys
sys.stdin = open('input.txt')

for _ in range(1, 11):
    tc = int(input())
    nums = [0] + list(map(int, input().split()))
    # print(nums)

    front = 0
    rear = len(nums) - 1
    minus_num = 1
    chg_num = deQueue()
    while chg_num - minus_num > 0:

        chg_num -= minus_num
        enQueue(chg_num)

        minus_num += 1
        if minus_num ==5:
            minus_num
        else:
            minus_num %= 5
        chg_num = deQueue()
    # print('changed:{}'.format(nums))
    # print(front, rear)
    print('#{}'.format(tc), end=' ')
    for idx in range(len(nums)-1):
        front += 1
        front %= len(nums)
        ans = nums[front]

        print(ans, end=' ')
    print()




