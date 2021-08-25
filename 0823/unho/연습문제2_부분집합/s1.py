'''
각 자릿수의 숫자가 포함되는지 안되는지 True False 값을 설정
현재 문제는 모든 부분집합을 구하므로 완전탐색
'''

#1. 내가 작성
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]
N = len(arr)
sel = [0] * N

def powerset(idx):
    #Base Case
    if idx == N:                        # 인덱스가 마지막+1 에 도착하면 끝내야함
        for i in range(N):              # 배열 요소만큼 반복
            if sel[i]:                  # 포함 여부 리스트의 해당 인덱스가 참이면 포함이므로
                print(arr[i], end=' ')  # 값 출력
        print()
    else:                               # 인덱스가 마지막이 아니면, 한 자릿수가 참 혹은 거짓으로 이동되므로 두가지 경우로 호출
        sel[idx] = 1                    # 현재 자릿수가 포함된다고 설정하고 다음 자릿수 호출
        powerset(idx+1)                 # 다음 자릿수 재귀함수 호출
        sel[idx] = 0                    # 함수 호출이 하나가 마무리 되면 마지막에 부른 함수에서 현재 자릿수 거짓으로 설정하고 다음 호출
        powerset(idx+1)                 # 다음 자릿수 재귀함수 호출

powerset(0)



# # 연습
#
# arr = [1, 2, 3]
# N = len(arr)
# sel = [0] * N
#
# def powerset(idx):
#     #Base Case
#     if idx == N:
#         for i in range(N):
#             if sel[i]:
#                 print(arr[i], end=' ')
#         print()
#
#     else:
#         sel[idx] = 1
#         powerset(idx+1)
#         sel[idx] = 0
#         powerset(idx+1)
#
# powerset(0)

# # 비트연산자 통한 부분집합 구하기 연습
# arr = [1, 2, 3]
# N = len(arr)
#
# for i in range(1<<N):
#     for j in range(N):
#         if i & (1<<j):
#             print(arr[j], end=' ')
#     print()