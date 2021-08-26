import sys
sys.stdin = open('input.txt')

for i in range(10):
    N = int(input())
    Nums = list(map(int,input().split()))
    while True:
        for k in range(1,6): # 5개의 숫자를 앞에서부터 1,2,3,4,5 씩 뺄것임으로 range를 1~5로 하기위하여 1,6으로 설정
            A = Nums.pop(0) - k # A = K 만큼 빼주면서
            if A <= 0: # A 0보다 작아지면
                A = 0 # A는 0으로 해줌
            Nums.append(A) # < 뺴준것을 맨뒤에 넣어주고
            if A == 0: # 만약 A가 0이면 바로 break(for)
                break

        if A == 0: # 와일문을 끝내기 위한 break
            break
    print('#{}'.format(i+1),end= ' ')
    for z in Nums:
        print(z,end=' ')
    print()
