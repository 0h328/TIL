#1-3. 중첩의 형태로 10*10의 경우를 모두 반복을 통해 찾아내기

# 5C2
arr = [3, 2, 8, 8, 8]
N = len(arr)

for i in range(N-1):
    for j in range(i+1, N):
        arr[i], arr[j] = arr[j], arr[i]
        # 한번 교환을 한 시점에서 다시 for문을 중첩하여 교환 진행
        # 10번의 교환에 다시 각 교환에 10번의 교환이 발생
        # 10 * 10 = 100번의 교환 발생
        for i in range(N-1):
            for j in range(i+1, N):
                arr[i], arr[j] = arr[j], arr[i]
                print(*arr)
                arr[i], arr[j] = arr[j], arr[i]
        arr[i], arr[j] = arr[j], arr[i]