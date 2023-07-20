# 이진탐색을 재귀로 생각해 보세요

def binarySearch(li, key, s, e):

    if s > e:
        return -1

    mid = (s+e)//2
    
    if key == li[mid]:
        return mid
    elif key < li[mid]:
        return binarySearch(li[:mid], key, 0, mid)
    else:
        return binarySearch(li[mid+1:], key, mid+1, len(li))
        

li = [5,6,10,11,21,9,15,13]
li.sort()

print("li =", li)

index = binarySearch(li, 9, 0, len(li))
print(index)