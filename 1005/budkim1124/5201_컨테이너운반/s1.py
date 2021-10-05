import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    n_list = sorted(list(map(int, input().split())), reverse=True) # 화물
    m_list = sorted(list(map(int, input().split())), reverse=True) # 트럭
    result = 0
    checked = [0] * N
    
    for i in range(M):
        for j in range(i, N):
            # 체크되어있으면 패스
            if checked[j]: 
                continue
            # 트럭이 더 클때만 옮김
            if m_list[i] >= n_list[j]:
                checked[j] = 1 
                result += n_list[j]  
                break
        if i == N:      # 같으면 다 돈거니까 break
            break

    print('#{} {}'.format(t+1, result))