# 회문 : 똑바로 읽으나 거꾸로 읽으나 똑같은 구문을 의미
def push(stack, n) :
    stack.append(n)

def enqueue(queue, n) :
    queue.append(n)

def isPal(word) :
    stack = []
    queue = []

    for w in word :
        if w.isalpha() :
            push(stack, w.lower())
            enqueue(queue, w.lower())

    # print(stack[::-1])
    # print(queue)

    if stack[::-1] == queue :
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
    "A man, a plan, a canal - Panama!"
]

for test in testCase :
    result = isPal(test)
    print(f"'{test}'(은)는 회문? {result}\n")