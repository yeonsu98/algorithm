# 하노이 타워

def hanoi(n, src, sub, dst): # (원판 개수, 출발지, 보조, 목적지)
    if n == 1:
        print(f"원판 {n} : {src} -> {dst}")
        return
    hanoi(n-1, src, dst, sub)
    print(f"원판 {n} : {src} -> {dst}")
    hanoi(n-1, sub, src, dst)

hanoi(1, 'A', 'B', 'C')
print()
hanoi(2, 'A', 'B', 'C')
print()
hanoi(3, 'A', 'B', 'C')
print()
