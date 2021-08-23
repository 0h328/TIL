# 재귀로 배열의 각 요소 출력
# 반드시 디버거를 활용하여 결과를 확인해주세요!!

a = [1, 2, 3]
N = len(a)

def f(i, N, a):
    if i == N:
        return # return None
    # else:
    print(a[i])
    f(i+1, N, a)
    # return이 없으면? None을 return

f(0, N, a)