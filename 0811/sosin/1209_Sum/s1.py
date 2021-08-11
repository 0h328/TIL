import sys
sys.stdin = open('input.txt')


for T in range(10):
    input()
    
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    row_sums = [0]*100
    col_sums = [0]*100
    diag_sums = 0
    rdiag_sums = 0
    for i in range(100):
        for j in range(100):
            temp = arr[i][j]
            row_sums[i]+=temp
            col_sums[j]+=temp
            if i==j:
                diag_sums+=temp
            if i==99-j:
                rdiag_sums+=temp

    print('#{} {}'.format((T+1), max(*row_sums, *col_sums, diag_sums, rdiag_sums)))
    
#1 1712
#2 1743
#3 1713
#4 1682
#5 1715
#6 1730
#7 1703
#8 1714
#9 1727
#10 1731
