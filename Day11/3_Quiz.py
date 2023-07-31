# Stack을 활용한 숫자 단위 찍기
# - 긴 길이의 숫자를 그냥 출력하면 가독성이 떨어진다
# - 따라서 긴 길이의 숫자는 우측에서 부터 3자리가 올 때마다 콤마(,)를 붙인다
# ex) 1000000000원 --> 1,000,000,000원

def push(stack, n):
    stack.append(n)

def pop(stack):
    return stack.pop()

def printStack(stack) :
    for n in stack[::-1]:
        print(f"│  {n:>3}  │")

    print("└───────┘")

def addComma(n) :
    stack = []
    result = ""
    count = 0

    while True :
        last = n % 10               # 끝 자리를 가져온다
        n //= 10                    # 기존의 숫자에서 끝 자리를 땐다

        push(stack, str(last))      # 떼어낸 끝 자리를 Stack에 추가
        count += 1                  # push 때마다 카운트를 증가

        if n == 0 : break           # 만약 원본(n)이 0이면 종료

        if count % 3 == 0 :         # 3개 추가될 때마다
            push(stack, ",")        # 콤마를 하나 추가


    while stack != [] :             # stack에서 모든 데이터를 꺼낸다
        result += pop(stack)        # 순서대로 꺼낸 값을 문자열에 누적

    return result



n = int(input())

n = addComma(n)
print("결과 :", n)