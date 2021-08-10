import sys

sys.stdin = open('input.txt')
data = list(map(int, input().split()))

def counting_sort(nums, max_num):   # counting sort는 집합 내 가장 큰 정수 알고 있어야 하므로 최대값 인자로 넘겨줌
    cnt = [0] * (max_num + 1)   # 최대값을 입력받았으므로 각 숫자들을 카운트할 리스트
    sorted_list = [0] * len(nums)   # 새로 정렬된 순서로 리스트 값 변경

    for num in nums:
        cnt[num] += 1

    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1]

    for j in range(len(nums)-1, -1, -1):
        sorted_list[cnt[nums[j]] - 1] = nums[j]
        cnt[nums[j]] -= 1

    return sorted_list

print('original: ', data)
max_num = max(data)
print('sorted: ', counting_sort(data, max_num))