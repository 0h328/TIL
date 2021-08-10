import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))

    def counting_sort(arr, max_num):
        count = [0] * (max_num + 1) # 최대값보다 1만큼 더한 칸 세팅

        for i in range(len(arr)): # 숫자 개수 세기
            count[arr[i]] += 1

        for i in range(max_num): # 숫자 개수 누적으로 세기
            count[i+1] += count[i]

        output = [-1] * len(arr) # 결과 리스트 세팅

        for i in arr: # 원래 리스트의 각 원소에 대해
            output[count[i] - 1] = i # count 리스트의 해당 값 -1 위치에 무조건 해당 원소
            count[i] -= 1 # count 리스트에서 하나 빼 줌, 중복 숫자 처리용

        return output

    max_num = max(arr)
    print(counting_sort(arr, max_num))