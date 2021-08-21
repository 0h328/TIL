# 동작 - 참조 가능
x = 10
def foo_bar():
    y = 2
    return x + y

print(foo_bar()) # 12

# 에러 - 변경 불가능
x = 10
def foo_bar():
    y = 2
    x += 2
    return x + y

print(foo_bar()) # UnboundLocalError: local variable 'x' referenced before assignment

# 해결 - 전역 변수 변경
x = 10
def foo_bar():
    global x
    y = 2
    x += 2
    return x + y

print(foo_bar()) # UnboundLocalError: local variable 'x' referenced before assignment

"""
> python의 `global` keyword

https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value

https://stackoverflow.com/questions/4693120/use-of-global-keyword-in-python
"""