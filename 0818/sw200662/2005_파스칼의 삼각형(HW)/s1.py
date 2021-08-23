import sys

sys.stdin = open('input.txt')

T = int(input())
list1 = [] # 전번단계의 리스트 저장
list2 = [] # 이번단계의 리스트 저장
for i in range(T):
    print('#{}'.format(i + 1))
    k = int(input())
    for a in range(0, k):
        list1 = list2[::] # list1이 2를 참조하지 않도록 softcopy 실행
        list2 = [1] * (a + 1) # list2를 초기화(1로 초기화해주는이유는 맨끝 1로 하기위해서)
        if a == 0 or a == 1: # 0or 1일때는 그냥 출력
            print(*list2)
        else:
            for c in range(1, a):
                list2[c] = list1[c - 1] + list1[c]
            print(*list2)
