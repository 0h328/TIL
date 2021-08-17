import sys
sys.stdin = open("input.txt")
#회문 검사 함수
def check(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[-i-1]:
            return False
    return True
#각 행에 대해서 검사할 것이기 때문에 가로기준 arr과 세로기준 arr2를 생성
for tc in range(1,11):
    T = int(input())
    arr = [list(input()) for _ in range(100)]
    #arr2는 arr의 전치행렬이다.
    arr2 = list(zip(*arr))
    max_v = 1 #길이가 1인 문자열 자체가 회문이므로 1로 초기화

#최대길이부터 거꾸로 검사한다
#해당 길이에서 최대값을 저장하게 되면 같은 길이나 그보다 작은 길이에서는
#검사할 필요가 없으므로 break선언


    for length in range(100,1,-1):
        if max_v >= length:
            break
        for idx in range(100-length+1):
            if max_v == length:
                break
            for lst, lst2 in zip(arr, arr2):
                if check(lst[idx:idx+length]) or check(lst2[idx:idx+length]):
                    max_v = length
                    break
    print('#{} {}'.format(tc,max_v))