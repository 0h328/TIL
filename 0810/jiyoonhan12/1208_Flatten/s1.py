import sys
sys.stdin = open('input.txt')

# counting 정렬 함수
def counting(arr):
    new_arr = [0] * len(arr)
    count = [0] * (max(arr) + 1)
    for i in range(len(arr)):
        count[arr[i]] += 1
    for i in range(len(count) - 1):
        count[i+1] += count[i]
    for i in range(len(arr)-1, -1, -1):
        new_arr[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return new_arr


for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    cnt = 0

    while cnt < dump: # cnt가 dump보다 작은 한 계속 실행
        boxes = counting(boxes) # sort 해주고
        boxes[len(boxes)-1] -= 1 # 최고값 -1
        boxes[0] += 1 # 최저값 +1
        cnt += 1
    else: # dump 초과하면
        boxes = counting(boxes) # 다시 한 번 sort 해주고
        sub = boxes[len(boxes)-1] - boxes[0] # 최고값과 최저값 빼줌

    print('#{} {}'.format(t, sub))