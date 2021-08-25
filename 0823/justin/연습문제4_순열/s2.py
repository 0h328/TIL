# 순열 - swap(라이브)

arr = [1, 2, 3]
N = len(arr)

def permutation(idx):
    if idx == N:                # idx는 자기 자신과 옆/그 옆.. 쭉 모든 경우와 바꿔봄
        print(*arr)
    else:
        for i in range(idx, N): # 현재 내 위치부터 다음까지 반복한다.(idx ~ N-1)
            arr[idx], arr[i] = arr[i], arr[idx] # 순서를 바꾸고
            permutation(idx+1)                  # 다음 확인하고
            arr[idx], arr[i] = arr[i], arr[idx] # 다음 순서를 위해 원복

permutation(0)