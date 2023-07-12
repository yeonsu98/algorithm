# 리스트를 사용한 하노이 시각화

import os
import time as t

def printHanoi():
    global A, B, C

    print("A =", A)
    print("B =", B)
    print("C =", C)

    if len(C) != 3:
        t.sleep(0.7)
        os.system("clear")

def hanoiMove(n, src, sub, dst):
    if n == 1:
        num = src.pop()
        dst.append(num)

        printHanoi()
        return
    hanoiMove(n-1, src, dst, sub)
    num = src.pop()
    dst.append(num)
    printHanoi()
    hanoiMove(n-1, sub, src, dst)

A = [i for i in range(5, 0, -1)]  # 출발지
B = []                            # 보조
C = []                            # 목적지


printHanoi()
hanoiMove(len(A), A, B, C)

