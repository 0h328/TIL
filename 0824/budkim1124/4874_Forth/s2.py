T = int(input())
for num in range(T):
    string = list(input().split())
    result = []
    ans = 0
    for i in range(len(string)-1):
        if string[i].isdigit():
            result.append(string[i])
        else:
            try:
                b, a = int(result.pop()), int(result.pop())
                if string[i] == '+':
                    c = a + b
                elif string[i] == '-':
                    c = a - b
                elif string[i] == '*':
                    c = a * b
                elif string[i] == '/':
                    c = a / b
                result.append(str(c))

            except:
                ans = -1
    if ans == -1 or len(result) >= 2:
        print("#{} {}".format(num+1, 'error'))
    else :
        print("#{} {}".format(num+1, int(result.pop())))