# Queue : 선입선출(FIFO)의 구조
def enqueue(queue, n) :
    queue.append(n)

def dequeue(queue) :
    return queue.pop(0)


queue = []

enqueue(queue, 10)      # queue의 입력 함수
enqueue(queue, 20)
enqueue(queue, 30)

print(queue)

print("\n꺼낸값 :", dequeue(queue))     # queue의 출력 함수
print(queue)

print("\n꺼낸값 :", dequeue(queue))
print(queue)

print("\n꺼낸값 :", dequeue(queue))
print(queue)