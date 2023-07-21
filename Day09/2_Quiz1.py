# quiz1.png
n = int(input())

li = list(map(int, input().split()))

li.sort()

result = 0  # 총 그룹 수
count = 0   # 한 그룹의 인원 수

for i in li :
    count += 1      # 현재 그룹의 인원 수 증가

    if i <= count:  # 그룹의 인원 수 공포도를 넘으면
        result += 1 # 그룹 하나를 결성
        count = 0   # 다음 그룹의 인원을 세기 위해 초기화

print(result)
