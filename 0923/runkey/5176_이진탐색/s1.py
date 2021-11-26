import sys
sys.stdin = open('input.txt')


"""
이진 트리에서 중위 순회를 할 시 루트 번호 계산 법
i 번째 숫자가 2, 5, 11, 23 ... 일 때는 숫자가 2의 제곱승이 올 때까지 유지
위의 숫자는 2 + 3 + 6 + 12+ ... 같은 규칙으로 이루어짐
2의 제곱승이 올 때는 위의 시작 숫자가 오기 전까지 루트 번호는 계속 상승함 
"""

root_list = [0]
square = 2
cnt = 0
start = 2
x = 1
flag = 0
for i in range(1, 100):
    if i % square == 0:
        square *= 2
        if i != 2:
            start += 3 * x
            x *= 2
        flag = 0

    if i == start:
        flag = 1
        cnt += 1

    if flag != 1:
        cnt += 1
    root_list.append(cnt)




def makeTree(n):
    global count
    #배열이니까 배열크기 넘어가지 않도록
    if n <= N:
        #왼쪽노드는 현재 인덱스의 2배
        makeTree(n*2)
        #더이상 못가면 값넣기
        tree[n] = count
        #값 넣었으면 증가시키기
        count += 1
        #우측 노드는 인덱스 2배 + 1
        makeTree(n*2 + 1)

tc = int(input())

for t in range(1, tc + 1):
    result = 0
    N = int(input())
    tree = [0 for i in range(N+1)]
    count = 1
    makeTree(1)
    result = tree[N//2]

    print("#{} {} {}".format(t, tree[1], result))