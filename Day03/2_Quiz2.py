# 사용자에게 로또 구매 개수를 입력받아서
# 해당 수만큼 로또 번호 화면에 출력
# 로또 추첨은 함수로 만들기

import random as r
import time as t

def getLotto():
    lotto = set()

    while len(lotto) != 6:
        lotto.add(r.randint(1, 45)) 

    lotto = list(lotto) 
    lotto.sort()
    return lotto

num = int(input("로또 구매 장 수 > "))

for i in range(1, num+1):
    lo = getLotto()
    print(f"{i}번째 lotto =", lo)

    t.sleep(1)

