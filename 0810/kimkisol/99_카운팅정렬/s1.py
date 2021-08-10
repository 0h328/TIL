import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def CountingSort(arr, reverse=False):
    cnt = [0] * (max(arr) + 1) #arr 안의 숫자 개수 셀 리스트
    result = [0] * len(arr) #결과 반환할 리스트
    #cnt리스트에 숫자 개수 채워넣기
    for num in arr:
        cnt[num] += 1
    #cnt리스트의 숫자 개수를 누적하여 저장
    for idx in range(1, len(cnt)):
        cnt[idx] += cnt[idx-1]
    #뒤에서부터 arr의 숫자의 누적개수를 찾아 해당 누적개수 - 1값의 인덱스에 arr 숫자 저장
    for idx in range(len(arr)):
        result[cnt[arr[idx]]-1] = arr[idx]
        cnt[arr[idx]] -= 1
    return result

arr = list(map(int, input().split()))
print(CountingSort(arr))