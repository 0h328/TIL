import sys
sys.stdin = open('input.txt')

# thought process:
# 인풋리스트A 가져오고
# 인풋 리스트안에 숫자들 카운트할 리스트B 만들고
# 인덱싱으로 각 A값 안의 숫자들이 확인 될 때마다
# B 리스트의 동일 숫자인 인덱스 값 +1
# B 리스트를 각 숫자를 더해서 재 정렬
# 같은 값이 있을경우 앞에 놓기 위해 거꾸로
# 숫자를 한개 넣을 공간을 만들어줌
# 해당 위치에 숫자를 삽입

# A = 인풋 리스트
A = list(map(int, input().split(', ')))
# B = 카운트 리스트
B = [0 for _ in range(len(A))]

for i in A:                             # 카운트 리스트에 카운트 값 저장
    B[i] += 1
print(B)

for i in range(len(B)-1):               # 이유 불문 카운트 리스트 누적합 구한다
    B[i+1] += B[i]
print(B)

for i in range(len(A)-1, -1, -1):       # 정렬된 B 를 거꾸로 순회하면서 정렬된 배열 C에 넣어준다
    B[]


# 정석적인 코드

#입력될 수 있는 숫자의 최대 크기
# MAX_NUM = 1000

# #A는 입력된 숫자를 저장하는 배열
# A = list(map(int, input().split()))
#
# #N은 입력된 숫자의 개수
# N = len(A)
#
# #0으로 초기화된 입력될 MAX_NUM+1 길이의 배열 count를 생성
# count =[0]*(MAX_NUM+1)
# #countSum은 누적합을 저장하는 배열
# countSum =[0]*(MAX_NUM+1)
#
# #숫자 등장 횟수 세기
# for i in range(0, N):
# 	count[A[i]] += 1
#
# #숫자 등장 횟수 누적합 구하기
# countSum[0] = count[0]
# for i in range(1, MAX_NUM+1):
# 	countSum[i] = countSum[i-1]+count[i];
#
# #B는 정렬된 결과를 저장하는 배열
# B = [0]*(N+1)
#
# for i in range(N-1, -1, -1):
# 	B[countSum[A[i]]] = A[i]
# 	countSum[A[i]] -= 1
#
# #수열 A를 정렬한 결과인 수열 B를 출력
# result = ""
# for i in range(1, N+1):
# 	result += str(B[i]) + " "
# print(result)
