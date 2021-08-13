import sys
sys.stdin = open("input.txt")

def selection_sort(nums):           # 선택정렬 = 최솟값을 찾아서 맨앞과 교환
    result = []
    for _ in range(len(nums)):      # nums 범위만큼 반복
        nums.sort()                 # nums를 정렬시킴
        result.append(nums.pop(0))  # nums의 0번째 인덱스 값을 제외시키면서 해당 값을 result에 담음
    return result                   # 정렬된 nums값들을 담은 result 리스트 반환

numbers = list(map(int, input().split()))
print(selection_sort(numbers))