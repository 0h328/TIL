import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    input()
    arr = list(map(int, input().split()))
    front = rear = -1
    button = 1

    while button:   # 0이 나올 때까지 계속 반복
        for i in range(1, 6):   # 1 사이클
            if arr[front + 1] - i > 0:          # 뺀 값이 0보다 크면
                arr.append(arr[front+1] - i)    # 뒤에 추가하고
                arr.pop(0)                      # 앞에서 제거
            else:               # 뺀 값이 0보다 작거나 같으면
                arr.append(0)   # 뒤에 0을 추가하고
                arr.pop(0)      # 앞에서 제거
                button = 0      # while문 반복 중지
                break           # for문 반복 중지

    print('#{}'.format(tc), end=' ')
    for num in arr:
        print(num, end=' ')
    print()

