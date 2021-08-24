# Dynamic Programming

def f(i, N, a):
    if i == N:  # 배열을 벗어나면(모든 원소에 대한 작업이 끝나면)
        return
    else:
        print(a[i])
        f(i + 1, N, a)  # 다음 원소로 이동


a = [10, 20, 30]
N = len(a)
f(0, N, a)