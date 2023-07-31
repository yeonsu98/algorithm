# 자료구조 : 데이터를 효율적으로 저장하기 위한 구조
# 1. 선형 구조 : Stack(스택), Queue(큐), List(리스트) 등
# 2. 비선형 구조 : Tree(트리), Graph(그래프) 등

# Stack : 선입후출(FILO)의 구조
# ※ Python은 List를 이용하면 손쉽게 구현 가능

def printStack(stack) :
    for n in stack[::-1]:
        print(f"│  {n:>3}  │")

    print("└───────┘")

def push(stack, n) :
    stack.append(n)

def pop(stack) :
    return stack.pop()


stack = []

push(stack, 10)     # stack의 입력 함수
push(stack, 20)
push(stack, 30)

printStack(stack)

print("\n꺼낸값 :", pop(stack))     # stack의 출력 함수
printStack(stack)

print("\n꺼낸값 :", pop(stack))
printStack(stack)

print("\n꺼낸값 :", pop(stack))
printStack(stack)