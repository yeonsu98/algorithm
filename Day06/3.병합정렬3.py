# 삽입 정렬과 병합 정렬의 시간 복잡도 테스트

import random as r
import time as t

def selectSort(li):
    for i in range(len(li)-1):
        for j in range(i+1, len(li)):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]

def mergeSort(li):
    if len(li) <= 1:
        return li
    
    mid = len(li) // 2

    left = mergeSort(li[:mid])
    right = mergeSort(li[mid:])

    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result

n = 10000
li1 = [r.randint(1, 100) for _ in range(n)]
li2 = li1[:] # 깊은 복사

start = t.time()
selectSort(li1)
end = t.time()
print(f"선택정렬 소요시간 : {end-start}초")

start = t.time()
li2 = mergeSort(li2)
end = t.time()
print(f"병합정렬 소요시간 : {end-start}초")