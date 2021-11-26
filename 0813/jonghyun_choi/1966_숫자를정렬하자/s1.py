import sys
sys.stdin = open('input.txt')

T = int(input())

for Case in range(T):
    N = int(input())
    num_list = list(map(int,input().split()))

    for i in range(len(num_list)-1):             # num_list를 순회합니다. 마지막은 자동으로 정렬되기 때문에 제외해줍니다.
        min_num = i                              # 해당 i(인덱스)를 min_num이란 변수에 초기화해줍니다.
        for j in range(i+1, len(num_list)):      # i(인덱스) 이후의 모든 값과 비교해 가장 작은 값의 인덱스를 min_num에 업데이트 해줍니다.
            if num_list[j] < num_list[min_num]:
                min_num = j
        num_list[i], num_list[min_num] = num_list[min_num], num_list[i]  # 안 쪽 반복문이 한 번 순회할 때마다 i 인덱스와 최소값인 j 인덱스를 교체해줌으로써 한 자리를 완성합니다.
    res = ' '.join(map(str,num_list))
    print('#{} {}'.format(Case+1,res))