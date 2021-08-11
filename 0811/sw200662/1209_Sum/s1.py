import sys
sys.stdin = open('input.txt')

def Sumlist(a):
    ansmax = sum(a[0]) # 맨 처음 초기화값
    temp_max3 = 0 # i = k > 대각선
    temp_max4 = 0 # i + k = 99 < 역대각선


    for i in range(100):
        temp_max = sum(a[i]) #행의 합
        temp_max2 = 0 #열의 값 초기화
        ans = []


        for k in range(100): # < 매 열계산시 열은 계산하여 구하고, 대각선 역대각선은 더해서 마지막에 max로 구함
            temp_max2 += a[k][i]
            if i == k:
                temp_max3 += a[i][k]
            if i + k == 99:
                temp_max4 += a[i][k]
        ans.extend([temp_max,temp_max2,temp_max3,temp_max4,ansmax])
        ansmax = max(ans)
    return(ansmax)

for i in range(10):
    test_case = int(input())
    lista = []
    for k in range(100):
        a = list(map(int,input().split()))
        lista.append(a)
    ans = Sumlist(lista)
    print('#{} {}'.format(i+1,ans))




