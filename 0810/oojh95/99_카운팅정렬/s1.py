import sys
sys.stdin = open('input.txt')

def countingsort(N, numbers):

    cnt_list = [0] * (max(numbers)+1) #카운팅 리스트를 초기화
    result = [0] * N # 정렬된 결과를 담기위한 리스트 초기화
    for num in numbers: # 카운트 리스트에 각 자리 수를 넣는다.
        cnt_list[num] += 1
    for i in range(1, max(numbers)+1):
        cnt_list[i] += cnt_list[i-1]

    for i in range(N-1, -1, -1):
        result[cnt_list[numbers[i]]-1] = numbers[i]
        cnt_list[numbers[i]] -= 1

    return result

N = int(input())
numbers = list(map(int, input().split()))
print(countingsort(N, numbers))