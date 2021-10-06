import sys
sys.stdin = open('input.txt')

# 합쳐서 소팅 함수
def merge(left, right):
    global answer
    if left[-1] > right[-1]:
        answer += 1

    merged_arr = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1

    merged_arr += left[l:]
    merged_arr += right[r:]
    return merged_arr

# 분할 후 합친 결과 확인 함수
def partition(arr):
    length = len(arr)
    if length < 2:
        return arr

    left_arr = arr[:length//2]
    right_arr = arr[length//2:]
    
    left_arr = partition(left_arr)
    right_arr = partition(right_arr)

    return merge(left_arr, right_arr)

for T in range(int(input())):
    answer = 0
    input()
    
    sorted_arr = partition(list(map(int, input().split())))
    
    print('#{} {} {}'.format((T+1), sorted_arr[len(sorted_arr)//2], answer))

#1 2 0
#2 6 6