# 다시 한번 구현
# 단, 랜덤으로 10개를 채우고 내림차순으로 출력

import random as r

def sortMerge(li):
    if len(li) <= 1:
        return li    
    mid = len(li) // 2

    left = sortMerge(li[:mid])
    right = sortMerge(li[mid:])

    result = []
    while left and right:
        if left[0] > right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right

    return result

li = [r.randint(1, 100) for _ in range(10)]
li = sortMerge(li)
print("li =", li)