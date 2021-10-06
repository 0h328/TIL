def enq(data):
    global hsize
    hsize += 1
    H[hsize] = item

    c = hsize
    p = hsize // 2

    while p and H[p] > H[c]:
        H[p], H[c] = H[c], H[p]
        c = p
        p = c // 2

def deq():
    global hsize
    tmp = H[1]
    H[1] = H[hsize]
    hsize -= 1
    p = 1
    c = p * 2  # 왼쪽자식번호를 먼저 계산해서

    while c <= hsize: # 왼쪽 자식이 있는지 확인
        if c + 1 <= hsize and H[c] > H[c + 1]: # 오른쪽 자식도 있고 오른쪽이 더 작으면 선택
            c += 1
        if H[p] > H[c]:  # 부모와 자식 비교
            H[p], H[c] = H[c], H[p] # 자식이 더 작으면 교환
            p = c           # 자리 바꿔서 자식 자리로 간 값과 그 자리의 자식번호 계산
            c = p * 2
        else:
            break

    return tmp

H = [7, 2, 3, 9, 5]