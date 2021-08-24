import sys
sys.stdin = open('input.txt')

num = list(map(int, input().split()))

def bubble_sort(num):

    for i in range(len(num)-1, 0, -1):                  # 전체 수행범위는 뒤에서부터 카운트
        for j in range(i):                              # 앞에서부터 두개씩 비교
            if num[j] > num[j+1]:                       # 앞 숫자가 크면
                num[j], num[j+1] = num[j+1], num[j]     # 앞뒤 숫자 바꾸기
    return num

print(bubble_sort(num))
