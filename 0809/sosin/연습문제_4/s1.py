import sys
sys.stdin = open('input.txt')

# 재귀함수구현
def is_babygin(arr, count):
    # 종료조건
    if count == 2:
        return 1
    else:
        # 배열의 길이만큼 돈다.
        for i in range(len(arr)):
            # 만약 현재 위치의 개수가 0보다 클 때
            if arr[i] > 0:
                # is_triplet
                if arr[i] >= 3:
                    # 기존 array를 변경하지 않기 위해 복사 후 처리
                    temp = arr.copy()
                    temp[i] -= 3
                    # 다음 판단으로 넘김
                    return is_babygin(temp, count+1)
                # is_run (배열 길이를 고려해 index=7까지만 체크)
                if i < 8 and arr[i+1] > 0 and arr[i+2] > 0:
                    temp = arr.copy()
                    temp[i]-=1
                    temp[i+1]-=1
                    temp[i+2]-=1
                    return is_babygin(temp, count+1)

    return 0

for _ in range(int(input())):
    counts = [0]*10
    for s in input():
        counts[int(s)] += 1
    
    print(is_babygin(counts, 0))