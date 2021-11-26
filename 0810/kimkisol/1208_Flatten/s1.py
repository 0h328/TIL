import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for t in range(1, 11):
    N = int(input())
    boxes = list(map(int, input().split()))
    #오름차순 정렬(버블 정렬)
    for i in range(len(boxes)-1, 0, -1):
        for j in range(i):
            if boxes[j] > boxes[j+1]:
                boxes[j], boxes[j+1] = boxes[j+1], boxes[j]
    #최고점은 마지막 idx, 최저점은 처음 idx에 초기화
    max_idx = len(boxes) - 1
    min_idx = 0
    # 덤프 횟수만큼
    for _ in range(N):
        #덤프하기
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        #max, min idx조정
        if boxes[max_idx] < boxes[max_idx-1]:
            max_idx -= 1
        else:
            max_idx = len(boxes) - 1
        if boxes[min_idx] > boxes[min_idx+1]:
            min_idx += 1
        else:
            min_idx = 0
        # 최고점과 최저점 차이가 1 또는 0일 때
        diff = boxes[max_idx] - boxes[min_idx]
        if diff < 2:
            break
    print('#{} {}'.format(t, diff))
