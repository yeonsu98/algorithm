# 1. 사용자에게 리스트 요소 개수를 입력 받음
n = int(input("리스트 요소 개수 입력 > "))

# 2. 1번에 입력한 수만큼 리스트 요소를 생성. 단, 랜덤으로 값을 채움
import random as r
li = [r.randint(1, 100) for _ in range(n)]

# 3. 리스트 출력
print("정렬 전 li =", li)
print("="*70)
# 4. 선택 정렬을 사용해서 내림차순 정렬 후 출력
import time

start = time.time()
for i in range(n-1):
    for j in range(i+1, n):
        if li[i] < li[j]:
            li[i], li[j] = li[j], li[i]
end = time.time()
print(f"선택 정렬 : {end - start:.5f} sec")
print("선택 정렬 후 li =", li)
print("="*70)

# 5. 삽입 정렬을 사용해서 오름차순 정렬 후 출력
start = time.time()
for i in range(1, len(li)):
    for j in range(0, i):
        if li[i] < li[j]:
            num = li.pop(i)
            li.insert(j, num)
end = time.time()
print(f"삽입 정렬 : {end - start:.5f} sec")
print("삽입 정렬 후 li =", li)
print("="*70)

# 6. 버블 정렬을 사용해서 내림차순 정렬 후 출력
start = time.time()
while True:
    cnt = 0
    for i in range(n-1):
        if li[i] < li[i+1]:
                li[i], li[i+1] = li[i+1], li[i] 
                cnt += 1
    if cnt == 0:
        break
end = time.time()
print(f"버블 정렬 : {end - start:.5f} sec")
print("버블 정렬 후 li =", li)
print("="*70)
