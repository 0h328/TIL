import sys
sys.stdin = open('input.txt')

def merge(lst):
    cnt = 0
    len_lst = len(lst)
    if len_lst <= 1:
        return lst, cnt
    else:
        left, left_cnt = merge(lst[: len_lst // 2])
        right, right_cnt = merge(lst[len_lst // 2:])

        my_lst = []
        left_idx = right_idx = 0
        right_is_small = False
        for _ in range(len_lst):
            if left_idx == len(left):
                my_lst.append(right[right_idx])
                right_idx += 1

            elif right_idx == len(right):
                my_lst.append(left[left_idx])
                left_idx += 1
                right_is_small = True

            elif left[left_idx] <= right[right_idx]:
                my_lst.append(left[left_idx])
                left_idx += 1

            else:
                my_lst.append(right[right_idx])
                right_idx += 1

        cnt = left_cnt + right_cnt
        if right_is_small:
            cnt += 1

        return my_lst, cnt


def sorted_merge(lst):
    sorted_lst, cnt = merge(lst)
    return sorted_lst[N // 2], cnt


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    print('#{}'.format(test_case), *sorted_merge(lst))