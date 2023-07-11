# 1. 정수를 입력 받아서 절댓값을 출력
n1 = int(input("1번 > "))
print("n =", n1 if n1>=0 else -n1)

# 2. 정수를 입력 받아서 1~n까지 일렬로 출력
n2 = int(input("2번 > "))
for i in range(1, n2+1):
    print(i, end=" ")
print()

# 3. 정수를 입력 받아서 약수를 출력
n3 = int(input("3번 > "))
for i in range(1, n3+1):
    if n3 % i == 0:
        print(i, end=" ")
print()

# 4. 정수를 전달하면 1~n까지의 합계를 반환
print("4번 > ", end=" ")
def total(num):
    sum = 0

    for i in range(1, num+1):
        sum += i

    return sum

result = total(5)
print(result)