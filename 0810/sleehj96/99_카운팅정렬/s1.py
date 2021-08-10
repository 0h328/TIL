import sys

sys.stdin = open('input.txt')

num_list = list(map(int, input().split()))


def counting_sort(lst):

    counts = [0] * (max(lst) + 1)       # counts 리스트 초기화

    for i in range(len(lst)):           # 해당 인덱스 값에 추가
        counts[lst[i]] += 1

    for j in range(1, len(counts)):
        counts[j] += counts[j-1]

    ans_list = [0] * len(lst)

    # print(lst)
    # print(list(reversed(lst)))

    for idx in reversed(lst):
        ans_list[counts[idx]-1] = idx
        counts[idx] -= 1

    return ans_list


print(counting_sort(num_list))
