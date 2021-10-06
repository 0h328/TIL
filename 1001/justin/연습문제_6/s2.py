"""
연습문제 6. Baby-gin
6-2) 재귀

베이비진이면 1
베이비진이 아니면 0
"""

"""
baby gin
arr = [6, 6, 7, 7, 6, 7]
arr = [0, 5, 4, 0, 6, 0]

baby gin x
arr = [1, 2, 4, 7, 8, 3]
rr = [1, 0, 1, 1, 2, 3]
"""

#2. baby gin - 재귀
"""
Baby gin Game Rule
 0에서 9사이의 숫자 카드에서 임의로 카드 6장을 뽑을 때
  - 3장의 카드가 연속적인 번호를 갖는 경우 run
  - 3장의 카드가 동일한 번호를 갖는 경우 triplete

가능한 조합
- run 2개
- triplete 2개
- run 1개 triplete 1개
"""

def baby_gin():
    global flag
    check = 0

    #1. 연속하는 3자리 수가 모두 같은 경우
    if arr[0] == arr[1] and arr[1] == arr[2]: check += 1
    if arr[3] == arr[4] and arr[4] == arr[5]: check += 1

    #2. 연속하는 세 자리수
    if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]: check += 1
    if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]: check += 1

    #3. 2개 나오는 경우 baby gin
    if check == 2:
        flag = 1
        return

# 순열
def perm(n, k):
    if n == k:
        baby_gin()
    else:
        for i in range(n, k):
            arr[k], arr[i] = arr[i], arr[k]  # 교환
            perm(n+1, k)                     # 다음 확인
            arr[k], arr[i] = arr[i], arr[k]  # 원상복구

# baby gin - o
arr = [6, 6, 7, 7, 6, 7]
# arr = [0, 5, 4, 0, 6, 0]

# baby gin - x
# arr = [1, 2, 4, 7, 8, 3]
# arr = [1, 0, 1, 1, 2, 3]
flag = 0
perm(0, len(arr)-1)

if flag:
    print('Baby Gin!')
else:
    print('Not Baby Gin!')