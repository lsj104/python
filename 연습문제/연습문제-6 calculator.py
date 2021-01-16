a = int(input("숫자 1을 입력해주세요:"))
b = int(input("숫자 2를 입력해주세요:"))
result = []

def add(a,b):
    result = a + b
    return result

def sub(a,b):
    result = a - b
    return result

def mul(a,b):
    result = a *b
    return result

def div(a,b):
    result = a / b
    return result

print(a, "+", b, "=", add(a,b))
print(a, "-", b, "=", sub(a,b))
print(a, "*", b, "=", mul(a,b))
print(a, "/", b, "=", div(a,b))
