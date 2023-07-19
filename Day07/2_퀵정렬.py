# 퀵정렬을 내림차순으로 다시 구현
# 단, 랜덤으로 채워서

import random as r

def quickSort(li):
    if len(li) <= 1:
        return li
    
    pivot = li[0]

    small, equal, big = [],[],[]

    for n in li:
        if n < pivot:
            small.append(n)
        elif n > pivot:
            big.append(n)
        else:
            equal.append(n)

    return quickSort(big) + equal + quickSort(small)
    


li = [r.randint(1, 100) for _ in range(10)]
print("정렬 전 > li =", li)
li = quickSort(li)
print("정렬 후 > li =", li)