import sys
sys.stdin = open('input.txt')

T = int(input()) # 전체 testcase

for test in range(1, T+1):
    box_row = int(input()) # 행 수
    room = list(map(int, input().split())) # 리스트로 만들기
    new_room = room[:] # 새 리스트에 복사

    # 정렬
    def BubbleSort(a):
        for i in range(len(a)-1, 0, -1):
            for j in range(0, i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]

    BubbleSort(new_room) # 복사해둔 리스트를 정렬
    fall = [] # 낙차 리스트

    for i in range(box_row): # 원래 리스트의 항목이 이동한 위치 찾기
        idx = new_room.index(room[i]) # 사실 index로 찾으면 중복값 고려 안 한 건데...
        fall.append(idx - i)

    max_fall = max(fall) # 가장 낙차가 큰 값
    print('#{} {}'.format(test, max_fall))
