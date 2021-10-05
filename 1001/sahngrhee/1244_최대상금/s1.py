import sys
sys.stdin = open('input.txt')


def my_swap(my_list):
    global cnt
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if len(priority[my_list[j]]) > 1:
                for sequence in priority[my_list[j]]:
                    if sequence == i and j in priority[my_list[i]]:
                        my_list[i], my_list[j] = my_list[j], my_list[i]
                        cnt -= 1
                    if not cnt:
                        return my_list
            else:
                if i in priority[my_list[j]]:
                    my_list[i], my_list[j] = my_list[j], my_list[i]
                    cnt -= 1
                if not cnt:
                    return my_list


T = int(input())

for test_case in range(1, T+1):
    num, cnt = map(int, input().split())
    nums = []
    while num > 0:
        nums = [num % 10] + nums
        num //= 10

    new_nums = reversed(sorted(nums))
    priority = {}
    for idx, val in enumerate(new_nums):
        priority[val] = priority.get(val, []) + [idx]

    print(my_swap(nums))


