"""
연습 문제2. 정렬 복습 - 정렬2
"""

#4. 병합 정렬
def merge(left, right):
    for i in range(left, right+1):
        for j in range(left+1, right+1-i):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return left

def partition(low, high):
    if high - low <= 1:
        print(low)
        return low

    mid = (low+high) // 2

    left = partition(low, mid)
    right = partition(mid, high)
    
    return merge(left, right)

numbers = [0, 55, 22, 33, 2, 1, 10, 26, 42]
print(numbers)               # 정렬 전
partition(0, len(numbers))
print(numbers)    # 정렬 후


#5. 퀵 정렬
def quick_sort():
    pass

def partition():
    pass

quick_nums = [0, 55, 22, 33, 2, 1, 10, 26, 42]