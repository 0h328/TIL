import sys
sys.stdin = open('input.txt')

def strangeSort(arr):
    arr.sort()
    result = [] # 결과를 저장할 리스트
    cnt = 0 # 카운팅 변수

    for small, large in zip(arr[:N // 2], reversed(arr[N//2:])): # 작은 수, 큰 수(역순)을 small, large로 받음
        result.append(large) # 큰 수부터 추가
        result.append(small) # 작은 수 추가
        cnt += 2 # 카운팅 +2
        if cnt >= 10: # 10보다 커지면 더 돌 필요 없음
            break
    else: # 만약, 10보다 작은 경우
        if N % 2: # 홀수인 경우
            result.append(arr[N//2]) # 중간 숫자 맨 뒤에 추가해야 함(zip 함수는 작은 쪽에 맞춰짐)

    return ' '.join(list(map(str, result[:10]))) # [] 없이 출력하기 위해 join 사용(join을 위해 내부 str로 변경)

T = int(input())
for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(test+1, strangeSort(arr)))

'''
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11 
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
'''

'''
import sys
sys.stdin = open('input.txt')

def strangeSort(arr):
    arr.sort()
    result = []

    if N % 2: # 홀수인 경우
        temp = arr[-1]
        del arr[-1]
        print(arr)
        print(arr[:N//2], list(reversed(arr[N//2:])), arr[N//2:-1:-1])
        for small, large in zip(arr[:N//2], reversed(arr[N//2:])):
            result.append(small)
            result.append(large)
        result.insert(0, temp)
        print(result, temp)
        return result
    else:
        pass



T = int(input())
for test in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    strangeSort(arr)
'''