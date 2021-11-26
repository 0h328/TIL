import sys
sys.stdin = open('input.txt')
A = list(map(int, input().split()))

def countingsort(A):                    #함수 구현, 버블과 차이점: 버블은 하나씩 오른쪽과 비교하는 느낌, 카운팅은 각 숫자가 들어가야할 좌석번호를 계산해서 넣어줌
    k = max(A)                          #리스트가 가지고 있는 최대 숫자 -> 그 숫자까지 정수 하나씩 카운팅 하는 용
    B = [0] * len(A)                    #정렬된 리스트가 담길 예정
    C = [0] * (k+1)                     #0부터 리스트가 가지고 있는 최대 숫자 k까지 각각 0을 C리스트에 담아둠

    for i in range(0, len(B)):         #정렬할 리스트 탐색, C 리스트에 저장 ex) 리스트 A에 7번째 요소가 3, 리스트 C의 idx가 3인 자리에 +1
        C[A[i]] += 1
    for i in range(1, len(C)):         # 0 1 2 3
        C[i] += C[i-1]                 #[0,1,3,4] 각각 해당하는 갯수 예시, [0, 1, 4, 8]로 합해줘서 3이 들어갈 자리를 알려 줌

    for i in range(len(B)-1,-1,-1):
        B[C[A[i]]-1] = A[i]            #A리스트에 오른쪽 숫자부터 하나씩 자리 확인 후 정렬된 리스트 자리에 넣어줌
        C[A[i]] -= 1                    # 입력 된 숫자는 -1해줌
    return B

print(Counting_Sort(A))


