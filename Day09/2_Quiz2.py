
n, m, k = map(int, input().split())
li = list(map(int, input().split()))

li = list(set(li))
li.sort(reverse=True)

first = li[0]      # 가장 큰 수
second = li[1]     # 두번째로 큰 수

result = 0

while True:
    for i in range(k):
        if m == 0: break

        result += first
        m  -= 1

    if m == 0: break
    
    result += second
    m -= 1


print(result)