# 1_Greedy.py는 결과적으로 보면 해는 맞다
# 하지만 매우 큰 숫자가 들어가면 매번 동전을 하나씩 차감하기 때문에
# 해를 구하는 속도가 매우 늦어지게 된다
# 아래는 알고리즘을 조금 개선한 버전이다

n = int(input("거슬러 줄 금액 : "))
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += n // coin
    n %= coin

print(count)