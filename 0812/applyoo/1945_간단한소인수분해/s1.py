import sys
sys.stdin = open('input.txt')

def Decomposition(Num):
    for i in prime_number:
        while Num % i == 0:                         # 해당 i로 안 나눠질 때까지
            prime_number[i] += 1                    # i(key)의 value를 +1
            Num = int(Num / i)

    result= []
    for i in [2, 3, 5, 7, 11]:                      # 딕셔너리 값 순서가 바뀌므로 정렬
        result.append(prime_number[i])
    return result

T = int(input())

for test in range(T):
    prime_number = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}  # Key = 소수, value = 갯수로 활용
    N = int(input())
    print('#{}'.format(test+1), *Decomposition(N))  # dict의 values를 원하는 형태로 출력하기 위해 출력 구분