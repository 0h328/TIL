# 재귀
def fibo_recursion(num):
    # nm <= 1:
    if num == 0 or num == 1:
        return num
    return fibo_recursion(num-1) + fibo_recursion(num-2)

print(fibo_recursion(10))
# print(fibo_recursion(50))