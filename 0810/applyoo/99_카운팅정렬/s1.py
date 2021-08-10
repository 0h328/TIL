import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))
new_arr = [0] * len(arr)
counting = [0] * (max(arr) + 1) # 최대값 + 1을 선언
print("테스트", "입력값\n", arr, '\n')

for i in arr: # 카운팅 구하기
    counting[i] += 1 # 해당 인덱스 값 +1
print("테스트", "카운팅\n", counting, '\n')

for i in range(1, len(counting)): # 누적합 구하기
    counting[i] += counting[i-1]
print("테스트", "구간 합\n", counting, '\n')

for i in reversed(arr): # arr값 역순으로 진행
    new_arr[counting[i]-1] = i # 인덱스 계산을 위해 -1
    counting[i] -= 1 # 입력값에 중복이 있을 경우를 방지하기 위해 -1

print("정답\n", new_arr)
# print(new_arr)