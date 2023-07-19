# 퀵 정렬
# - 이름에 따라서 가장 빠른 속도를 자랑하는 알고리즘
# - 비균등 분할 알고리즘
# - 단, 이미 정렬된 리스트에 쓰면 O(n^2)의 시간 복잡도가 걸리게 됨
# - 퀵 정렬은 pivot(피봇)을 기준으로 리스트를 분할

def quickSort(li):
    if len(li) <= 1:
        return li
    
    pivot = li[len(li)//2]
    # pivot을 구하는 알고리즘이 있지만
    # 파이썬은 리스트로 쉽게 구현 가능

    small, equal, big = [], [], []

    for n in li:
        if pivot < n:
            big.append(n)
        elif pivot > n:
            small.append(n)
        else: 
            equal.append(n)

    return quickSort(small) + equal + quickSort(big)

li = [21,10,12,20,25,13,15,22]

li = quickSort(li)
print("li =", li)

# li.sort()
# print("li =", li)

# li.reverse()
# print("li =", li)