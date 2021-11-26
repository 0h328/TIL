#1-2. 실제 문제에 적용

# 5C2
arr = [3, 2, 8, 8, 8]
N = len(arr)

for i in range(N-1):                            # 첫 번째 요소 뽑기 -> 가장 뒤에서 하나 앞(N-2)를 남겨놓고 뽑고
    for j in range(i+1, N):                     # 두 번째 요소 뽑기 -> 가장 뒤(N-1)를 남겨놓고 뽑기
        arr[i], arr[j] = arr[j], arr[i]         # 교환
        print(*arr)
        arr[i], arr[j] = arr[j], arr[i]         # 다음 교환을 위해서 원상 복구하는 작업