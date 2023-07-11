# 로또 추첨기
# 알고리즘)
# 1. 숫자 1 ~ 45 사이의 숫자를 무작위로 뽑는다
# 2. 개수는 6개를 뽑으며 중복은 뽑을 수 없다.
# 3. 추첨 결과는 항상 오름차순으로 발표

import random as r

result = []
while len(result) != 6:
    num = r.randint(1, 45)
    if num not in result:
        result.append(num)
result.sort()
print("로또 추첨 결과 = ", result)

print("="*50)

lotto = set()

while len(lotto) != 6:
    n = r.randint(1, 45)
    lotto.add(n)

lotto = list(lotto)
lotto.sort()
print("lotto =", lotto)



