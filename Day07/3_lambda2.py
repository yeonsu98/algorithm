# 람다식은 변수에 저장하고 사용
# 주로 다른 함수의 매개변수에서 람다식을 받아 처리

def func(n1, fn):
    return n1 + fn(5, 3)

result = func(8, lambda x, y : x ** y)
print("result =", result)