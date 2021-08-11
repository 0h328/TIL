import sys
sys.stdin = open('input.txt')

data_list = list(map(int,input().split()))

for i in range(len(data_list)-1,0,-1):  # 한 바퀴를 돌 때마다 한 개의 위치가 정해짐
    for j in range(i):                  # 이 경우는 매 순회마다 오른쪽 끝 index의 값이 정해짐
        if data_list[j] > data_list[j+1]:  # j는 아직 값이 정해지지 않은 index까지 순회하며 자신의 바로 뒤에 있는 값과 비교
            data_list[j], data_list[j+1] = data_list[j+1], data_list[j] # 값 비교 후 두 개를 크기 순으로 정렬
print(data_list)