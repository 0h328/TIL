import sys
sys.stdin = open('input.txt')


def counting_sort(A, k):
    C = [0] * (k + 1)  # 카운트하기 위한 빈 리스트 생성
    result = [0] * len(A)

    for i in range(0, len(A)):  # A의 개수를 센다
        C[A[i]] += 1  # for문 내에서 C리스트에 카운트한다. ## A[i]가 들어간 이유는 인덱스 값과 A리스트의 값과 맞춰줘야하기 때문

    for i in range(1, len(C)):  # C에 누적하여 입력한다.
        C[i] += C[i-1]

    for i in range(len(result) -1, -1, -1):  #
        result[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

    return A, C, result


arr = list(map(int, input().split()))
print(counting_sort(arr, 5))