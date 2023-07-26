# 회문 : 똑바로 읽으나 거꾸로 읽으나 똑같은 구문을 의미

def push(stack, n):
    stack.append(n)

def pop(stack):
    return stack.pop()

def enqueue(queue, n):
    queue.append(n)

def dequeue(queue):
    return queue.pop(0)

def isPal(word):
    stack = []
    queue = []

    for w in word:
        if w.isalpha():
            push(stack, w.lower())
            enqueue(queue, w.lower())

    # print(stack[::-1])
    # print(queue)
    # 파이썬은 slicing이 있기 때문에 pop이 필요없음

    # print(stack[::-1] == queue) # level -> True, Level -> False

    if stack[::-1] == queue:
        return True
    
    return False

testCase = [
    "level",
    "다시 합창합시다",
    "소주 만 병만 주소",
    "여보 안경 안 보여",
    "Madam, I'm Adam.",
    "nurses run",
    "Was it a cat I saw?",
    "A man, a plan, a canal - panama!"
]

for test in testCase:
    result = isPal(test)
    print(f"{test}는 회문입니까? > {result}")