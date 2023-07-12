# 1. 절대값은 음수에 -부호를 취하거나
n = int(input("정수 입력 : "))

if n < 0 :
    n *= -1

print("n =", n)


# 2. 제곱 후 제곱근을 취하는 방식으로 얻을 수 있다
import math as m

n = int(input("\n다시 입력 : "))

n **= 2
n = int(m.sqrt(n))   # sqrt() : 제곱근을 반환

print("n =", n)


# ※ 절대값은 자주 사용되는 기능이라 Python에는 기본 제공
n = abs(-10)

print("n =", n)